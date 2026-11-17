import time

from decorator_drills import timer


@timer
def slow_add(a, b):
    """Add two numbers slowly."""
    time.sleep(0.1)
    return a + b


def test_returns_result() -> None:
    assert slow_add(1, 2) == 3
    assert slow_add(a=1, b=2) == 3


def test_preserves_metadata() -> None:
    assert slow_add.__name__ == "slow_add"
    assert slow_add.__doc__ == "Add two numbers slowly."


def test_prints_timing(capsys) -> None:
    slow_add(1, 2)
    out = capsys.readouterr().out
    assert "slow_add took" in out
    assert out.endswith("s\n")


def test_exposes_wrapped(capsys) -> None:
    result = slow_add.__wrapped__(1, 2)

    assert result == 3
    assert capsys.readouterr().out == ""
