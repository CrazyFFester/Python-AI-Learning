import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    assert Jar(5).capacity == 5
    assert Jar(0).capacity == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar(2.5)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1)

    assert jar.size == 5


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)

    jar.withdraw(3)
    assert jar.size == 0
