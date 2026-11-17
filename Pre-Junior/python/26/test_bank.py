from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("HELLO there") == 0


def test_h():
    assert value("h") == 20
    assert value("hey") == 20
    assert value("How you doing?") == 20


def test_other():
    assert value("What's happening") == 100
    assert value("") == 100
    assert value("123") == 100
