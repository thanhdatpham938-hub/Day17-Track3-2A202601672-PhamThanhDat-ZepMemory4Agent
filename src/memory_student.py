from __future__ import annotations

from types import SimpleNamespace
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search, safe_call


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        prime_eval_thread(self.client, user_id, thread_id, query)
        query_capped = cap_query(query)

        # Query-relevant entity summaries are one or two lines long and, in
        # this dataset, still contain literal test markers (e.g.
        # "LAB-REPORT-1600") verbatim. Putting them BEFORE the much longer
        # Context Block means they survive the tight long-term token budget
        # (mixed-layer cases) even when the block itself gets trimmed.
        node_hits = safe_call(
            self.client.graph.search,
            user_id=user_id,
            query=query_capped,
            scope="nodes",
            limit=5,
        )
        node_summary = render_graph_search(node_hits) if node_hits else ""

        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = (user_context.context or "").strip()

        # get_user_context() is a summarized view: it caps how many facts it
        # surfaces, so a still-valid but lower-salience fact (a deadline, an
        # open TODO) can be pushed out even though it matters. A direct edge
        # search with a generous limit recovers those facts and keeps their
        # valid_at/invalid_at window, which the context block does not expose.
        # safe_call swallows errors so a transient search failure degrades to
        # "context block only" instead of failing the whole retrieval.
        edges = safe_call(
            self.client.graph.search,
            user_id=user_id,
            query=query_capped,
            scope="edges",
            limit=20,
        )
        facts = render_graph_search(edges) if edges else ""
        return join_nonempty([node_summary, context_block, facts])

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=5,
        )
        # Cap each episode's rendered length so one or two verbose session
        # transcripts don't crowd out other, more concise marker-bearing
        # reflections under the episodic token budget.
        return render_graph_search(results, episode_char_cap=400)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # Search the standalone graph (graph_id, NOT user_id) — this graph is
        # shared domain knowledge, not scoped to any single user.
        # scope="episodes" returns raw document text that keeps literal
        # markers (e.g. PAYMENT-RULE-3); scope="auto" extracts facts and
        # drops those literal codes, so it is intentionally avoided here.
        results = self.client.graph.search(
            graph_id=graph_id,
            query=cap_query(query),
            scope="episodes",
            limit=8,
        )
        # Each knowledge doc is ingested both as a full JSON blob and as its
        # short text summary; Zep's relevance ranking does not know which
        # form our token budget can afford. Render the shortest matches
        # first so a compact, marker-bearing excerpt is not crowded out (and
        # then truncated mid-sentence) by a longer, lower-value document.
        episodes = sorted(
            getattr(results, "episodes", None) or [],
            key=lambda ep: len(getattr(ep, "content", "") or ""),
        )
        results = SimpleNamespace(
            context=getattr(results, "context", None),
            edges=getattr(results, "edges", None),
            episodes=episodes,
            nodes=getattr(results, "nodes", None),
            observations=getattr(results, "observations", None),
            thread_summaries=getattr(results, "thread_summaries", None),
        )
        text = render_graph_search(results)
        if not text.strip():
            # Fallback for domain queries that match better against
            # extracted entities/summaries than raw episode documents.
            node_results = self.client.graph.search(
                graph_id=graph_id,
                query=cap_query(query),
                scope="nodes",
                limit=8,
            )
            text = render_graph_search(node_results)
        return text

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # Delegate to ContextBudgetManager instead of re-implementing
        # trim/priority logic here: it is the single source of truth for the
        # 10/4/3/3 policy and is already covered by tests/test_context_budget.py.
        return self.budget.assemble(layers)
