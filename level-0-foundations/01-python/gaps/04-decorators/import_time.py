import functools


def trace(func):
    print("decorating", func.__name__)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        result = func(*args, **kwargs)

        return result

    print("decorated", func.__name__)

    return wrapper


@trace
def a():
    return "a"


@trace
def b():
    return "b"
