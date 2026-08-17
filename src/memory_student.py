from __future__ import annotations

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
            query=cap_query(query),
            scope="edges",
            limit=20,
        )
        facts = render_graph_search(edges) if edges else ""
        return join_nonempty([context_block, facts])

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
