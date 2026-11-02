import re


class Time:
    def __init__(self, hours: str, minutes: str | None, meridiem: str) -> None:
        if int(hours) not in range(1, 12 + 1):
            raise ValueError("Wrong Format")

        self.hours: int = int(hours)

        if minutes is not None:
            if int(minutes) in range(0, 59 + 1):
                self.minutes: int = int(minutes)
            else:
                raise ValueError("Wrong Format")
        else:
            self.minutes = 0

        self.meridiem: str = meridiem

    def to_24h(self) -> str:
        hours_24h: int = self.hours

        if self.meridiem == "PM":
            if hours_24h == 12:
                hours_24h = 0
            hours_24h += 12

        if hours_24h == 12 and self.meridiem == "AM":
            hours_24h = 0

        return f"{hours_24h:02}:{self.minutes:02}"


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(?P<hours_from>\d{1,2})(?::(?P<minutes_from>\d{2}))? "
        r"(?P<meridiem_from>AM|PM) to (?P<hours_to>\d{1,2})"
        r"(?::(?P<minutes_to>\d{2}))? (?P<meridiem_to>AM|PM)",
        s,
    )

    if match is None:
        raise ValueError("Wrong format")

    hours_from, meridiem_from = (
        int(match["hours_from"]),
        match["meridiem_from"],
    )
    hours_to, meridiem_to = (int(match["hours_to"]), match["meridiem_to"])
    minutes_from = 0
    minutes_to = 0

    if hours_from in range(1, 12 + 1) and hours_to in range(1, 12 + 1):
        if match["minutes_from"] is not None:
            minutes_from = int(match["minutes_from"])

            if minutes_from not in range(0, 59 + 1):
                raise ValueError("Wrong Format")

        if match["minutes_to"] is not None:
            minutes_to = int(match["minutes_to"])

            if minutes_to not in range(0, 59 + 1):
                raise ValueError("Wrong Format")

    else:
        raise ValueError("Wrong format")

    if meridiem_from == "PM":
        if hours_from == 12:
            hours_from = 0
        hours_from += 12

    if meridiem_to == "PM":
        if hours_to == 12:
            hours_to = 0
        hours_to += 12

    if hours_from == 12 and meridiem_from == "AM":
        hours_from = 0

    if hours_to == 12 and meridiem_to == "AM":
        hours_to = 0

    return f"{hours_from:02}:{minutes_from:02} to {hours_to:02}:{minutes_to:02}"


if __name__ == "__main__":
    main()
