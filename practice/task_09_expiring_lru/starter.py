class ExpiringLRUCache:
    def __init__(self, capacity: int):
        raise NotImplementedError
    def put(self, key, value, ttl: float, now: float) -> None:
        raise NotImplementedError
    def get(self, key, now: float):
        raise NotImplementedError
    def delete(self, key) -> bool:
        raise NotImplementedError
    def keys(self, now: float) -> list:
        raise NotImplementedError
