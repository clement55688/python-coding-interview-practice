def run_robot(
    width: int,
    height: int,
    obstacles: set[tuple[int, int]],
    commands: list[str],
    start: tuple[int, int] = (0, 0),
    heading: str = "N",
) -> dict:
    raise NotImplementedError
