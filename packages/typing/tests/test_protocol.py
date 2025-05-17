from src.protocol import foo

class MockBar():
    def __init__(self) -> None:
        ...

    def baz(self) -> None:
        print("MockBar.baz called")

class InvalidMockBar():
    def piyo(self) -> None:
        print("InvalidMockBar.piyo called")


def test_foo():
    mock_bar = MockBar()
    foo(mock_bar)
    _invalid__mock_bar = InvalidMockBar()
    # foo(invalid__mock_bar)

