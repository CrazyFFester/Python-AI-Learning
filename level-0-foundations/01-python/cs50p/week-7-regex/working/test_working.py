import pytest

from working import convert


@pytest.mark.parametrize(
    "time, expected",
    [
        ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
        ("9 AM to 5 PM", "09:00 to 17:00"),
        ("9:00 AM to 5 PM", "09:00 to 17:00"),
        ("9 AM to 5:00 PM", "09:00 to 17:00"),
        ("10:30 AM to 4:45 PM", "10:30 to 16:45"),
    ],
)
def test_valid(time: str, expected: str) -> None:
    assert convert(time) == expected


@pytest.mark.parametrize(
    "time, expected",
    [
        ("12 AM to 12 PM", "00:00 to 12:00"),
        ("12:30 PM to 12:45 AM", "12:30 to 00:45"),
        ("1 AM to 1 PM", "01:00 to 13:00"),
        ("11:59 AM to 11:59 PM", "11:59 to 23:59"),
        ("10 PM to 8 AM", "22:00 to 08:00"),
    ],
)
def test_edge_values(time: str, expected: str) -> None:
    assert convert(time) == expected


@pytest.mark.parametrize(
    "time",
    [
        "0 AM to 12 PM",
        "12 PM to 0 AM",
        "13 PM to 12 PM",
        "12 PM to 13 PM",
        "12:60 PM to 1:00 PM",
        "1:00 PM to 12:60 PM",
    ],
)
def test_invalid_time(time: str) -> None:
    with pytest.raises(ValueError):
        convert(time)


@pytest.mark.parametrize(
    "time",
    [
        "12:30 AM - 1 PM",
        "12:30 AM  1 PM",
        "12:30 AM to 1",
        "12:30 to 1 PM",
        "09:00 to 17:00",
        "12:30PM to 1 PM",
        "",
        "cat",
    ],
)
def test_invalid_format(time: str) -> None:
    with pytest.raises(ValueError):
        convert(time)
