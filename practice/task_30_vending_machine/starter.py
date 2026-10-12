class VendingMachine:
    def __init__(self, catalog: dict[str, dict[str, int]]):
        raise NotImplementedError

    def insert_coin(self, coin: int) -> int:
        raise NotImplementedError

    def select(self, code: str) -> dict:
        raise NotImplementedError

    def refund(self) -> list[int]:
        raise NotImplementedError

    def snapshot(self) -> dict:
        raise NotImplementedError
