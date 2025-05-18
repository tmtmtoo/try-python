from typing import Callable


def foo(bar: Callable[[], int], factor: int) -> Callable[[], int]:
    def wrapper() -> int:
        return bar() * factor

    return wrapper
