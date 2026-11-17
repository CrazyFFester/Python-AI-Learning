import pytest

from jar import Jar


def test_init_default() -> None:
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0


@pytest.mark.parametrize("capacity", [0, 5])
def test_init_valid(capacity) -> None:
    jar = Jar(capacity)

    assert jar.capacity == capacity


@pytest.mark.parametrize("capacity", [-1, "-5", 2.5])
def test_init_invalid(capacity) -> None:
    with pytest.raises(ValueError):
        jar = Jar(capacity)


@pytest.mark.parametrize(
    "cookies, expected", [(1, "🍪"), (2, "🍪🍪"), (3, "🍪🍪🍪"), (0, "")]
)
def test_str(cookies, expected) -> None:
    jar = Jar()
    jar.deposit(cookies)
    assert str(jar) == expected


@pytest.mark.parametrize("n", [0, 5, 12])
def test_deposit_valid(n) -> None:
    jar = Jar()
    jar.deposit(n)

    assert jar.size == n


@pytest.mark.parametrize(
    "first, second, expected", [(2, 3, 5), (5, 7, 12), (0, 4, 4)]
)
def test_deposit_accumulates(first, second, expected) -> None:
    jar = Jar()
    jar.deposit(first)
    jar.deposit(second)

    assert jar.size == expected


@pytest.mark.parametrize("n", [6, -1, 2.5, "1"])
def test_deposit_invalid(n) -> None:
    jar = Jar(5)

    with pytest.raises(ValueError):
        jar.deposit(n)


def test_deposit_overflow_accumulated() -> None:
    jar = Jar()
    jar.deposit(7)

    with pytest.raises(ValueError):
        jar.deposit(6)

    assert jar.size == 7


@pytest.mark.parametrize(
    "deposited, withdrawn, expected", [(5, 2, 3), (5, 5, 0), (5, 0, 5)]
)
def test_withdraw_valid(deposited, withdrawn, expected) -> None:
    jar = Jar()
    jar.deposit(deposited)
    jar.withdraw(withdrawn)

    assert jar.size == expected


def test_withdraw_accumulates() -> None:
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    jar.withdraw(7)

    assert jar.size == 0


@pytest.mark.parametrize("n", [4, -1, 2.5, "1"])
def test_withdraw_invalid(n) -> None:
    jar = Jar()
    jar.deposit(3)

    with pytest.raises(ValueError):
        jar.withdraw(n)

    assert jar.size == 3
