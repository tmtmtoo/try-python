from src.callable import foo


def test_foo():
    wrapped_function = foo(lambda: 42, factor=2)
    result = wrapped_function()
    assert result == 84, f"Expected 84, but got {result}"


def test_foo2():
    def mock_bar():
        return 42

    wrapped_function = foo(mock_bar, factor=3)
    result = wrapped_function()
    assert result == 126, f"Expected 126, but got {result}"
