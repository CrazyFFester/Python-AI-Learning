import functools


def retry(times, exceptions):
    if times < 1:
        raise ValueError(f"times must be >= 1, got {times}")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    continue
            return func(*args, **kwargs)

        return wrapper

    return decorator
