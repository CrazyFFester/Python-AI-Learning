import pytest

from numb3rs import validate


@pytest.mark.parametrize(
    "ipv4", ["0.0.0.0", "255.255.255.255", "127.0.0.1", "192.168.1.10"]
)
def test_valid(ipv4: str) -> None:
    assert validate(ipv4) is True


@pytest.mark.parametrize(
    "ipv4",
    [
        "256.1.1.1",
        "1.256.1.1",
        "1.1.256.1",
        "1.1.1.256",
        "1.2.3.1000",
        "1.2.3",
        "1.2.3.4.5",
        "1.2.3.",
        "",
        "cat",
        "1.2.3.a",
        "1.2.3.-4",
        "1 .2.3.4",
        "192.168.001.1",
        "01.2.3.4",
        "1.2.3.00",
    ],
)
def test_invalid(ipv4: str) -> None:
    assert validate(ipv4) is False
