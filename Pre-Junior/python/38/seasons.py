import re
import sys
from datetime import date

import inflect


def parse_birth_date(dob: str) -> date:
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", dob):
        raise ValueError("Invalid date")
    return date.fromisoformat(dob)


def minutes_between(birth: date, today: date) -> int:
    return (today - birth).days * 24 * 60


def minutes_to_words(minutes: int) -> str:
    words = inflect.engine().number_to_words(
        minutes,  # pyright: ignore[reportArgumentType]
        andword="",
    )
    assert isinstance(words, str)
    return f"{words.capitalize()} minutes"


def main() -> None:
    try:
        birth_date = parse_birth_date(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_to_words(minutes_between(birth_date, date.today())))


if __name__ == "__main__":
    main()
