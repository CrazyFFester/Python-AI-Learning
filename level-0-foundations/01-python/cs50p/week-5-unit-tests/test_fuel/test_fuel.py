import pytest

from fuel import convert, gauge


def test_convert_zero_denominator() -> None:
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


@pytest.mark.parametrize("fraction", ["5/4", "cat/dog", "1.5/3", "-1/4"])
def test_convert_value_error(fraction: str) -> None:
    with pytest.raises(ValueError):
        convert(fraction)


@pytest.mark.parametrize(
    "percentage, expected",
    [(1, "E"), (99, "F"), (0, "E"), (100, "F"), (50, "50%")],
)
def test_gauge(percentage: int, expected: str) -> None:
    assert gauge(percentage) == expected


@pytest.mark.parametrize(
    "fraction, expected",
    [("1/2", 50), ("3/4", 75), ("2/3", 67), ("0/4", 0), ("4/4", 100)],
)
def test_convert(fraction: str, expected: int) -> None:
    assert convert(fraction) == expected
