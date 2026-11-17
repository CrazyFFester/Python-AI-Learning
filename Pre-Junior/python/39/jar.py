class Jar:
    def __init__(self, capacity: int = 12) -> None:
        if type(capacity) is not int:
            raise ValueError("Capacity is not integer")
        if capacity < 0:
            raise ValueError("Negative capacity")
        self._capacity: int = capacity
        self._cookies: int = 0

    def __str__(self) -> str:
        return "🍪" * self._cookies

    def deposit(self, n: int) -> None:
        if type(n) is not int:
            raise ValueError("Amount is not integer")
        if n < 0:
            raise ValueError("Negative number")
        if (self._cookies + n) > self._capacity:
            raise ValueError("Out of capacity")
        self._cookies += n

    def withdraw(self, n: int) -> None:
        if type(n) is not int:
            raise ValueError("Amount is not integer")
        if n < 0:
            raise ValueError("Negative number")
        if self._cookies - n < 0:
            raise ValueError("More than have in jar")
        self._cookies -= n

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def size(self) -> int:
        return self._cookies
