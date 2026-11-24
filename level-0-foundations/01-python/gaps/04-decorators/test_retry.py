import pytest

from retry import retry


@pytest.fixture
def make_flaky():
    def make(fail_times, exc=ValueError):
        calls = 0

        def flaky():
            """Fails fail_times times, then returns "ok"."""
            nonlocal calls

            calls += 1
            if calls <= fail_times:
                raise exc(calls)
            return "ok"

        def get_calls():
            return calls

        return flaky, get_calls

    return make


class TestRetry:
    def test_success_first_try(self, make_flaky) -> None:
        flaky, get_calls = make_flaky(fail_times=0)
        wrapped = retry(times=3, exceptions=(ValueError,))(flaky)
        assert wrapped() == "ok"
        assert get_calls() == 1

    @pytest.mark.parametrize(("times", "fail_times"), [(3, 2), (5, 4), (5, 1)])
    def test_success_after_failures(self, make_flaky, times, fail_times) -> None:
        flaky, get_calls = make_flaky(fail_times=fail_times)
        wrapped = retry(times=times, exceptions=(ValueError,))(flaky)
        assert wrapped() == "ok"
        assert get_calls() == fail_times + 1

    def test_exhausted_reraises_last(self, make_flaky) -> None:
        flaky, get_calls = make_flaky(fail_times=10)
        wrapped = retry(times=2, exceptions=(ValueError,))(flaky)

        with pytest.raises(ValueError, match="^2$"):
            wrapped()

        assert get_calls() == 2

    def test_other_exception_not_retried(self, make_flaky) -> None:
        flaky, get_calls = make_flaky(fail_times=1, exc=TypeError)
        wrapped = retry(times=3, exceptions=(ValueError,))(flaky)

        with pytest.raises(TypeError, match="^1$"):
            wrapped()

        assert get_calls() == 1

    @pytest.mark.parametrize("times", [0, -1])
    def test_invalid_times(self, times) -> None:
        with pytest.raises(ValueError, match="times must be >= 1"):
            retry(times=times, exceptions=(ValueError,))

    def test_preserves_metadata(self, make_flaky) -> None:
        flaky, _ = make_flaky(fail_times=0)
        wrapped = retry(times=3, exceptions=(ValueError,))(flaky)
        assert wrapped.__name__ == "flaky"
        assert wrapped.__doc__ == flaky.__doc__
        assert wrapped.__wrapped__ is flaky
