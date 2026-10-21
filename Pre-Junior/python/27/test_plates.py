import pytest
from plates import is_valid


@pytest.mark.parametrize("plate", ["A", "ABCDEFG", ""])
def test_length(plate):
    assert not is_valid(plate)


@pytest.mark.parametrize("plate", ["50CS", "C50", "1A"])
def test_starts_with_two_letters(plate):
    assert not is_valid(plate)


@pytest.mark.parametrize(
    "plate, expected",
    [
        ("CS50", True),
        ("AAA222", True),
        ("AAA22A", False),
        ("CS50P", False),
        ("AB1C2", False),
        ("CS5", True),
    ],
)
def test_numbers_at_end(plate, expected):
    assert is_valid(plate) == expected


@pytest.mark.parametrize("plate", ["CS05", "CS0"])
def test_first_number_not_zero(plate):
    assert not is_valid(plate)


@pytest.mark.parametrize("plate", ["CS 50", "CS.50", "PI3.14", "HI!"])
def test_no_punctuation_or_spaces(plate):
    assert not is_valid(plate)


@pytest.mark.parametrize("plate", ["AA", "ABCDEF"])
def test_length_bounds_valid(plate):
    assert is_valid(plate)
