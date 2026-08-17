# README_submission

## Phân tích benchmark (reports/benchmark.json, --impl student)

Kết quả: 11/11 PASS, hit rate 100%, avg latency 698ms, avg token reduction 20.2%.

1. **Layer hit rate thấp nhất:** không layer nào FAIL (100% cả 4 layer). Layer rủi ro nhất là `long_term`: xử lý cả conflict/recency (E08) lẫn isolation (E09) trong cùng hàm `retrieve_long_term`, nên một lỗi ở đây làm fail nhiều case cùng lúc.
2. **Query tốn token nhất:** E03 "Minh còn open loop hay deadline nào chưa hoàn thành?" — 1316 retrieved tokens, vì Context Block trả về toàn bộ USER_SUMMARY + FACTS + ENTITIES + THREADS thay vì chỉ phần liên quan tới open loop.
3. **E07 (mixed):** cần kết hợp `long_term` (preference Python của Minh) + `semantic` (quy tắc payment retry). Evidence bắt buộc: `Python`, `Idempotency-Key`. Budget breakdown: long_term 1307→324 tokens (bị trim theo limit 320), semantic 148/148 tokens (không trim).
4. **Token reduction:** trung bình 20.2% (memory-enabled) so với 81.8% ở no-memory baseline (reports/comparison.md). No-memory "giảm" nhiều chỉ vì gần như không retrieve gì — hit rate tương ứng chỉ 18.2% (2/11, đúng 2 case short-term không cần Zep). Reduction chỉ có ý nghĩa khi đi kèm hit rate cao; giảm token mà mất evidence là vô dụng.

## Reflection bắt buộc

- **Layer quan trọng nhất:** `long_term` — quyết định trực tiếp 4/11 case (E02, E03, E08, E09) và là một trong hai layer bắt buộc của E07, tổng cộng ảnh hưởng 5/11 case.
- **Trade-off Zep Context Block vs Redis+Qdrant:** Zep tự lo compaction, conflict resolution theo recency, graph relevance — tiết kiệm code nhưng mỗi call ~700-1500ms, phụ thuộc dịch vụ ngoài. Redis+Qdrant latency thấp (dưới 1ms), toàn quyền kiểm soát dữ liệu, nhưng phải tự viết dedup/conflict/re-rank.
- **Guardrail chống memory poisoning:** `control_plane/AGENTS.md` yêu cầu mọi durable write giữ source/timestamp/confidence/scope; `heartbeat.py --dry-run` chỉ de-dup và đánh dấu stale, không tự thêm instruction/quyền mới; `privacy_guard.py` chặn ingest nếu user chưa opt-in (`data/consent.json`) và tự redact PII (email/phone).

**E08 (recency):** fact "prioritizes Python" cũ bị `invalid_at` đánh dấu hết hiệu lực từ 2026-08-05, đúng lúc fact mới "BLUEBIRD-42 requires TypeScript/NestJS" xuất hiện — nhưng fact "Python cho ORCHID-27" (project khác) vẫn `invalid_at=None`. Recency chỉ override đúng scope, không xóa preference ở project không liên quan.

**E10 (compaction):** `ShortTermMemory` (sliding) trải qua 8 lần compaction, chỉ giữ 6 tin nhắn gần nhất, nhưng `DURABLE_NOTES` vẫn giữ "REVIEW-DEADLINE-1600" — compaction ưu tiên constraint bền vững thay vì xóa theo thời gian đơn thuần.
