class DNAIndex:
    def __init__(self, sequences: dict[str, str], k: int):
        raise NotImplementedError

    def search(self, query: str) -> list[str]:
        raise NotImplementedError
