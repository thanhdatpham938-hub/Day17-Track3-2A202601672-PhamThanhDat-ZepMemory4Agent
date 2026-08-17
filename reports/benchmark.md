# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **832.6 ms**
- Average token reduction vs full source context: **15.0%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| E06 | semantic | PASS | 767.5 | 148 | 67.8% |  |
| E09 | long_term | PASS | 1456.5 | 915 | 0.0% |  |
| E10 | short_term | PASS | 0.5 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1480.3 | 1837 | 0.0% |  |
| E03 | long_term | PASS | 1486.7 | 1830 | 0.0% |  |
| E04 | episodic | PASS | 236.3 | 202 | 8.6% |  |
| E05 | episodic | PASS | 242.0 | 241 | 0.0% |  |
| E07 | mixed | PASS | 1746.7 | 485 | 14.2% |  |
| E11 | semantic | PASS | 292.2 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1449.8 | 1826 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata=`

### E09 - long_term

`ENTITY: LOTUS-88 - LOTUS-88 is Lan Tran's project. ENTITY: Lan Tran - Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for this purpose. ENTITY: Da hieu - Da hieu provided backend examples in Java + Spring Boot. ENTITY: Java - Lan Tran prioritizes Java for her project. ENTITY: Spring Boot - Lan Tran prioritizes Spring Boot for her project. <USER_SUMMARY> Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for this purpose. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     S`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by Friday at 16:00. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When explaining c`

### E03 - long_term

`ENTITY: client lifecycle - Hay kiem tra lifecycle cua client. ENTITY: concurrency - Hay kiem tra concurrency. ENTITY: coroutine - Minh Nguyen is studying async/await and often confuses coroutines with Tasks. Minh asked for an explanation of this topic via a timeline if encountered in the future. ENTITY: timeout - Minh Nguyen attempted to increase the timeout to 60 seconds while debugging async HTTP, but it still failed. ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and `

### E04 - episodic

`EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, dung tron Lan. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. EPISODE: Toi dang `

### E05 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong playbook truoc khi noi timeout. Dung lay stack cua ai khac. EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, d`

### E07 - mixed

`<LONG_TERM> ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by Friday at 16:00. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When `

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata=`

### E08 - long_term

`ENTITY: BLUEBIRD-42 - Da tach scope uses BLUEBIRD-42 for dung TypeScript/NestJS and ORCHID-27 for priority Python. ENTITY: NestJS - NestJS is required for the backend of the BLUEBIRD-42 company project. ENTITY: TypeScript - TypeScript is required for the backend of the BLUEBIRD-42 company project. Python is not to be used for the backend of this project, but Python is still preferred for personal ORCHID-27 demos. ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggest`
