from typing import Protocol

class Bar(Protocol):
    def baz(self) -> None:
        ...

def foo(bar: Bar) -> None:
    bar.baz()

