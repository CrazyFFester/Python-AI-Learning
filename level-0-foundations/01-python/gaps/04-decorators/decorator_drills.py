import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start

        print(f"{func.__name__} took {elapsed:.4f}s")

        return result

    return wrapper


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1  # pyright: ignore[reportAttributeAccessIssue]
        return func(*args, **kwargs)

    wrapper.calls = 0  # pyright: ignore[reportAttributeAccessIssue]

    return wrapper


def count_calls_nonlocal(func):
    calls = 0

    def get_calls() -> int:
        return calls

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal calls

        calls += 1
        return func(*args, **kwargs)

    wrapper.get_calls = get_calls  # pyright: ignore[reportAttributeAccessIssue]

    return wrapper
