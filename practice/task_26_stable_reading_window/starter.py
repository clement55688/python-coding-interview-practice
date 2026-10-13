from collections import deque

def longest_stable_window(readings: list[float], max_spread: float) -> tuple[int, int]:
    if isinstance(max_spread, bool) or not isinstance(max_spread, (int, float)):
        raise ValueError("max_spread must be numeric")

    if max_spread < 0:
        raise ValueError("max_spread must be nonnegative")

    if not readings:
        return (0, 0)

    for reading in readings:
        if isinstance(reading, bool) or not isinstance(reading, (int, float)):
            raise ValueError("readings must be numeric")

    max_deque = deque()
    min_deque = deque()

    left = 0
    best_start = 0
    best_end = 0

    for right, reading in enumerate(readings):
        while max_deque and readings[max_deque[-1]] <= reading:
            max_deque.pop()
        max_deque.append(right)

        while min_deque and readings[min_deque[-1]] >= reading:
            min_deque.pop()
        min_deque.append(right)

        while readings[max_deque[0]] - readings[min_deque[0]] > max_spread:
            left += 1

            while max_deque and max_deque[0] < left:
                max_deque.popleft()

            while min_deque and min_deque[0] < left:
                min_deque.popleft()

        if right - left + 1 > best_end - best_start:
            best_start = left
            best_end = right + 1

    return (best_start, best_end)