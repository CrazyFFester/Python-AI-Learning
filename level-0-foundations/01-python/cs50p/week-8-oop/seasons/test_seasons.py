from datetime import date

import pytest

from seasons import parse_birth_date, minutes_between, minutes_to_words


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("1999-05-01", date(1999, 5, 1)),
        ("2005-06-12", date(2005, 6, 12)),
        ("2000-02-29", date(2000, 2, 29)),
    ],
)
def test_parse_valid_date(input_date, expected) -> None:
    assert parse_birth_date(input_date) == expected


@pytest.mark.parametrize(
    "input_date",
    [
        "19999-05-01",
        "1-05-01",
        "sfdsfew",
        "1999-April-12",
        "19990101",
        "1999-W01-1",
        "1999W011",
        "1999-W01",
        "1999W01",
    ],
)
def test_parse_invalid_format(input_date) -> None:
    with pytest.raises(ValueError):
        parse_birth_date(input_date)


@pytest.mark.parametrize(
    "input_date", ["2001-02-29", "2005-23-59", "0000-01-01"]
)
def test_parse_nonexistent_date(input_date) -> None:
    with pytest.raises(ValueError):
        parse_birth_date(input_date)


@pytest.mark.parametrize(
    "birth, today, expected",
    [
        (date(2000, 1, 1), date(2000, 1, 1), 0),
        (date(2000, 1, 1), date(2000, 1, 2), 1440),
        (date(1999, 1, 1), date(2000, 1, 1), 525600),
        (date(2000, 1, 1), date(2001, 1, 1), 527040),
    ],
)
def test_minutes_between(birth, today, expected) -> None:
    assert minutes_between(birth, today) == expected


def test_minutes_between_returns_int() -> None:
    assert type(minutes_between(date(1999, 1, 1), date(2000, 1, 1))) is int


@pytest.mark.parametrize(
    "minutes, expected",
    [
        (23, "Twenty-three minutes"),
        (
            6_250_500,
            "Six million, two hundred fifty thousand, five hundred minutes",
        ),
        (525_600, "Five hundred twenty-five thousand, six hundred minutes"),
    ],
)
def test_minutes_to_words(minutes, expected) -> None:
    assert minutes_to_words(minutes) == expected
