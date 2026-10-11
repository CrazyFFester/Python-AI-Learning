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

try:
    row_date = input("Date: ")
    day = 0
    month = 0
    year = 0

    if match := re.search(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", row_date):
        month, day, year = map(int, match.groups())
    elif match := re.search(r"^(\d{1,2} (\[a-z]+) (\d{4}$", row_date,
                            re.IGNORECASE):
        month_name = match.group(2).title()

        if month not in months:
            raise ValueError()
except ValueError as error:
    print(error)

print(f"{year:04}-{month:02}-{day:02}")
