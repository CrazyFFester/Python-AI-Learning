import time

import pytest

from decorator_drills import count_calls, count_calls_nonlocal, timer


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
        result = slow_add.__wrapped__(1, 2)  # pyright: ignore[reportFunctionMemberAccess]

        assert result == 3
        assert capsys.readouterr().out == ""


class TestCountCalls:
    @pytest.fixture
    def greet(self):
        @count_calls
        def greet(name) -> str:
            return f"hi {name}"

        return greet

    def test_counts_calls(self, greet) -> None:
        for _ in range(3):
            greet("Emir")
        assert greet.calls == 3

    def test_starts_at_zero(self, greet) -> None:
        assert greet.calls == 0

    def test_returns_result(self, greet) -> None:
        assert greet("Emir") == "hi Emir"

    def test_preserves_name(self, greet) -> None:
        assert greet.__name__ == "greet"

    def test_counts_failed_calls(self) -> None:
        @count_calls
        def boom() -> None:
            raise ValueError("boom")

        with pytest.raises(ValueError, match="boom"):
            boom()

        assert boom.calls == 1  # pyright: ignore[reportFunctionMemberAccess]


class TestCountCallsNonlocal:
    @pytest.fixture
    def greet(self):
        @count_calls_nonlocal
        def greet(name) -> str:
            return f"hi {name}"

        return greet

    def test_counts_calls(self, greet) -> None:
        for _ in range(3):
            greet("Emir")

        assert greet.get_calls() == 3

    def test_starts_at_zero(self, greet) -> None:
        assert greet.get_calls() == 0
