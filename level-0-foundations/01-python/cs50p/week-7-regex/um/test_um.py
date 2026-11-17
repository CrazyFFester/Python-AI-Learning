from um import count


def test_single() -> None:
    assert count("um") == 1


def test_in_middle() -> None:
    assert count("yummy") == 0
    assert count("umbrella album") == 0


def test_multiple() -> None:
    assert count("um ummy um, hmm, Helllom") == 2


def test_case_insensitive() -> None:
    assert count("Um, UM, uM") == 3
