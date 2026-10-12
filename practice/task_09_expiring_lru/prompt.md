# Module 09: Expiring LRU cache

Original practice exercise; not an actual Benchling interview question.

Implement `ExpiringLRUCache(capacity)` with `put(key, value, ttl, now)`, `get(key, now)`, `delete(key)`, and `keys(now)`.

- Capacity must be a positive integer; TTL must be positive.
- An item is expired when `now >= expires_at`.
- `get` returns `None` for missing/expired keys. A successful get makes the key most recently used.
- `put` replaces an existing key and makes it most recent. Before enforcing capacity, purge all expired entries. Then evict least recently used live entries.
- `keys` purges expired entries and returns keys from least to most recently used.
- Passing time backwards relative to the last operation that accepts `now` raises `ValueError`.

Aim for O(1) average `get` and `put`, excluding the cost of purging expired entries.
