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


def main() -> None:
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    match: re.Match[str] | None = re.fullmatch(
        r"(?P<hours_from>\d{1,2})(?::(?P<minutes_from>\d{2}))? "
        r"(?P<meridiem_from>AM|PM) to (?P<hours_to>\d{1,2})"
        r"(?::(?P<minutes_to>\d{2}))? (?P<meridiem_to>AM|PM)",
        s,
    )

    if match is None:
        raise ValueError("Wrong Format")

    time_from: Time = Time(
        match["hours_from"], match["minutes_from"], match["meridiem_from"]
    )
    time_to: Time = Time(
        match["hours_to"], match["minutes_to"], match["meridiem_to"]
    )

    return f"{time_from.to_24h()} to {time_to.to_24h()}"


if __name__ == "__main__":
    main()
