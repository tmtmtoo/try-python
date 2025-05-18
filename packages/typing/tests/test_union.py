from src.union import hoge, Foo, Bar, Baz


def test_hoge():
    foo_instance = hoge(Foo(bar=42, baz="hello"))
    assert foo_instance == "Foo: 42, hello"

    bar_instance = hoge(Bar(foo=3.14))
    assert bar_instance == "Bar: 3.14"

    baz_instance = hoge(Baz(qux=Bar(foo=2.71)))
    assert baz_instance == "Baz: 2.71"
