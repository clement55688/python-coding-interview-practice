class ElevatorController:
    def __init__(self, floor_count: int):
        raise NotImplementedError

    def request(self, floor: int) -> None:
        raise NotImplementedError

    def step(self) -> dict:
        raise NotImplementedError

    def snapshot(self) -> dict:
        raise NotImplementedError
