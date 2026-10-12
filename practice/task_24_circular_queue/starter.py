class CircularQueue:
    def __init__(self, capacity: int):
        raise NotImplementedError

    def enqueue(self, value) -> bool:
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def front(self):
        raise NotImplementedError

    def rear(self):
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
