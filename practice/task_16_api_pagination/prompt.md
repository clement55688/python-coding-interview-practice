# 01 — Paginated experiment API

Implement `collect_experiments(fetch_page, start_cursor=None, max_retries=2)`.

`fetch_page(cursor)` returns a dictionary:

```python
{"items": [{"id": "e1", "name": "Run 1"}], "next_cursor": "abc"}
```

Requirements:

- Follow `next_cursor` until it is `None`.
- Retry `TimeoutError` up to `max_retries` times for each cursor. `max_retries=2` means one initial call plus two retries.
- Propagate other exceptions immediately.
- Deduplicate items by `id`, keeping the first occurrence and original order.
- Raise `ValueError` for missing/non-string IDs, malformed pages, a repeated cursor, or negative `max_retries`.
- Return new dictionaries so callers cannot mutate the fetcher's originals.

Discuss request count, memory, retry policy, backoff, and how you would test a real HTTP adapter without making network calls.
