import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

day = 0
month = 0
year = 0

try:
    row_date = input("Date: ")

    if match := re.search(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", row_date):
        month, day, year = map(int, match.groups())
    elif match := re.search(r"^([a-z]+) (\d{1,2}), (\d{4})$", row_date,
                            re.IGNORECASE):
        month_name = match.group(1).title()

        if month_name not in months:
            raise ValueError()

        month = months.index(month_name) + 1
        day = int(match.group(2))
        year = int(match.group(3))
except ValueError as error:
    print(error)

print(f"{year:04}-{month:02}-{day:02}")
