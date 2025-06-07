from callee import miracle_function


def test_miracle_function():
    msg = miracle_function()
    assert len(msg) > 0
