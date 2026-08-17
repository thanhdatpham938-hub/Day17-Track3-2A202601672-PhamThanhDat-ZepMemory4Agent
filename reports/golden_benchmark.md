# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1054.7 ms**
- Average token reduction vs full source context: **7.7%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.5 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1567.1 | 928 | 0.0% |  |
| G09 | semantic | PASS | 248.1 | 365 | 20.5% |  |
| G10 | semantic | PASS | 204.9 | 217 | 52.7% |  |
| G14 | mixed | PASS | 1573.5 | 553 | 0.0% |  |
| G03 | long_term | PASS | 1446.7 | 1908 | 0.0% |  |
| G04 | long_term | PASS | 1426.8 | 1886 | 0.0% |  |
| G07 | episodic | PASS | 233.8 | 189 | 14.5% |  |
| G08 | episodic | PASS | 224.5 | 190 | 14.0% |  |
| G11 | mixed | PASS | 1594.8 | 569 | 0.0% |  |
| G13 | mixed | PASS | 566.4 | 442 | 21.8% |  |
| G15 | mixed | PASS | 1814.7 | 782 | 0.0% |  |
| G16 | mixed | PASS | 1593.3 | 581 | 0.0% |  |
| G17 | mixed | PASS | 1726.0 | 581 | 0.0% |  |
| G18 | mixed | PASS | 456.0 | 500 | 11.5% |  |
| G19 | mixed | PASS | 1834.6 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1399.2 | 1866 | 0.0% |  |
| G12 | mixed | PASS | 1563.2 | 507 | 19.8% |  |
| G20 | mixed | PASS | 1620.7 | 756 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`ENTITY: Lan Tran - Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for this purpose. ENTITY: Da hieu - Da hieu provided backend examples in Java + Spring Boot. ENTITY: Java - Lan Tran prioritizes Java for her project. ENTITY: Python - Lan Tran does not use Python in the backend for her project. ENTITY: Spring Boot - Lan Tran prioritizes Spring Boot for her project. <USER_SUMMARY> Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for this purpose. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At`

### G09 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","upd`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G14 - mixed

`<LONG_TERM> ENTITY: Lan Tran - Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for this purpose. ENTITY: Lab Assistant - Lab Assistant identifies Da hieu. ENTITY: Da hieu - Da hieu provided backend examples in Java + Spring Boot. ENTITY: Java - Lan Tran prioritizes Java for her project. ENTITY: Python - Lan Tran does not use Python in the backend for her project. <USER_SUMMARY> Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for this purpose. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: `

### G03 - long_term

`ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by Friday at 16:00. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When explaining c`

### G04 - long_term

`ENTITY: Task - Minh Nguyen is learning async/await and often confuses coroutine with Task. Minh requested that if this topic arises later, it should be explained using a timeline. ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by Friday at 16:00. For the compan`

### G07 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? `

### G08 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi?`

### G11 - mixed

`<LONG_TERM> ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by Friday at 16:00. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When `

### G13 - mixed

`<EPISODIC> EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi preference cua Minh, dung tron so thich dong nghiep. EPISODE: Mai hop mentor, toi nay minh muon don open-loop. Liet ke viec chua dong, deadline, va ma`

### G15 - mixed

`<LONG_TERM> ENTITY: async HTTP - Minh Nguyen debugged async HTTP today. Minh attempted to increase the timeout to 60 seconds, but it still failed. ENTITY: timeout - Minh Nguyen attempted to increase the timeout to 60 seconds while debugging async HTTP, but it still failed. ENTITY: timeout threshold - Minh Nguyen stated that the timeout threshold was not the main issue, identifying connection churn instead. This was in the context of ASYNC-FIX-20. ENTITY: async/await - Minh Nguyen is learning async/await and often confuses coroutine with Task. Minh requested that if this topic arises later, it should be explained using a timeline. ENTITY: ASYNC-FIX-20 - Minh Nguyen identified connection churn`

### G16 - mixed

`<LONG_TERM> ENTITY: Task - Minh Nguyen is learning async/await and often confuses coroutine with Task. Minh requested that if this topic arises later, it should be explained using a timeline. ENTITY: async HTTP - Minh Nguyen debugged async HTTP today. Minh attempted to increase the timeout to 60 seconds, but it still failed. ENTITY: coroutine - Minh Nguyen is learning async/await and often confuses coroutine with Task. Minh requested that if this topic arises later, it should be explained using a timeline. ENTITY: LAB-REPORT-1600 - LAB-REPORT-1600 is an open loop benchmark report that must be completed before Thursday at 16:00. ENTITY: timeout threshold - Minh Nguyen stated that the timeout `

### G17 - mixed

`<LONG_TERM> ENTITY: coroutine - Minh Nguyen is learning async/await and often confuses coroutine with Task. Minh requested that if this topic arises later, it should be explained using a timeline. ENTITY: async/await - Minh Nguyen is learning async/await and often confuses coroutine with Task. Minh requested that if this topic arises later, it should be explained using a timeline. ENTITY: concurrency - Hay kiem tra concurrency. ENTITY: timeout threshold - Minh Nguyen stated that the timeout threshold was not the main issue, identifying connection churn instead. This was in the context of ASYNC-FIX-20. ENTITY: async HTTP - Minh Nguyen debugged async HTTP today. Minh attempted to increase the `

### G18 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi preference cua Minh, dung tron so thich dong nghiep. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong playbook truoc khi noi t`

### G19 - mixed

`<LONG_TERM> ENTITY: async HTTP - Minh Nguyen debugged async HTTP today. Minh attempted to increase the timeout to 60 seconds, but it still failed. ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by Friday at 16:00. For the company project BLUEBIRD-42, the backen`

### G05 - long_term

`ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by Friday at 16:00. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27.  Minh prefers Python and dislikes Java. When explaining c`

### G12 - mixed

`<LONG_TERM> ENTITY: NestJS - TypeScript with NestJS is required for the BLUEBIRD-42 company project backend, and Python is not to be used for its backend. Python is still used for personal demos like ORCHID-27. ENTITY: Minh Nguyen - The user is working on a personal project named ORCHID-27 and is debugging an async HTTP issue, identified as ASYNC-FIX-20. They are also learning about async/await and coroutines versus Tasks. The user has tried increasing the timeout to 60 seconds and suggests reusing an aiohttp ClientSession with concurrency set to 20. The core issue is identified as connection churn, not the timeout threshold. The user is also working towards completing a benchmark report by `

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
