from src.foo import pow, add


def test_pow():
    assert pow(2, 3) == 8


def test_add():
    assert add(2, 3) == 5
