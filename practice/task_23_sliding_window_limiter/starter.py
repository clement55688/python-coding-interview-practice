class RateLimiter:
    def __init__(self, limit: int, window_seconds: float):
        raise NotImplementedError

    def allow(self, key: str, timestamp: float) -> bool:
        raise NotImplementedError
