import time

import pytest

from decorator_drills import count_calls, timer


@timer
def slow_add(a, b):
    """Add two numbers slowly."""
    time.sleep(0.1)
    return a + b


class TestTimer:
    def test_returns_result(self) -> None:
        assert slow_add(1, 2) == 3
        assert slow_add(a=1, b=2) == 3

    def test_preserves_metadata(self) -> None:
        assert slow_add.__name__ == "slow_add"
        assert slow_add.__doc__ == "Add two numbers slowly."

    def test_prints_timing(self, capsys) -> None:
        slow_add(1, 2)
        out = capsys.readouterr().out
        assert "slow_add took" in out
        assert out.endswith("s\n")

    def test_exposes_wrapped(self, capsys) -> None:
        result = slow_add.__wrapped__(1, 2)

        assert result == 3
        assert capsys.readouterr().out == ""


class TestCountCalls:
    @pytest.mark.skip(reason="TODO: write tests for count_calls")
    def test_todo(self) -> None: ...
