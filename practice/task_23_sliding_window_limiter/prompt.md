# 23 — Sliding-window rate limiter

Implement `RateLimiter(limit, window_seconds)` with `allow(key, timestamp)`.

- Each key may have at most `limit` allowed events in the half-open window `(timestamp - window_seconds, timestamp]`.
- An event exactly `window_seconds` old has expired.
- Only allowed events consume capacity.
- Timestamps must be numeric and globally nondecreasing across all calls.
- Keys must be non-empty strings.
- Reject booleans where a numeric value is expected.
- Raise `ValueError` for invalid constructor arguments or calls.

Use Python standard-library data structures. Explain why a deque supports amortized O(1) processing and what memory remains after old events expire.

Follow-up: discuss how this design changes across multiple servers.
