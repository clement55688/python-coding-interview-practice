class PhaseCycle:
    def __init__(self, phases: list[tuple[str, int]]):
        raise NotImplementedError

    def tick(self, count: int = 1) -> dict:
        raise NotImplementedError

    def update_duration(self, name: str, duration: int) -> dict:
        raise NotImplementedError

    def snapshot(self) -> dict:
        raise NotImplementedError
