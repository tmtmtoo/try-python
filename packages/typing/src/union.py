from dataclasses import dataclass
from typing import Literal, assert_never


@dataclass
class Foo:
    bar: int
    baz: str
    tag: Literal["foo"] = "foo"


@dataclass
class Bar:
    foo: float
    tag: Literal["bar"] = "bar"


@dataclass
class Baz:
    qux: Bar
    tag: Literal["baz"] = "baz"


Hoge = Foo | Bar | Baz


def hoge(value: Hoge) -> str:
    match value.tag:
        case "foo":
            return f"Foo: {value.bar}, {value.baz}"
        case "bar":
            return f"Bar: {value.foo}"
        case "baz":
            return f"Baz: {value.qux.foo}"
        case _:
            assert_never(value)
