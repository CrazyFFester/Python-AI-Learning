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

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = map(int, date.split("/"))
        else:
            month, day, year = date.split()

            if not day.endswith(","):
                continue

            month = months.index(month) + 1
            day = int(day[:-1])
            year = int(year)

        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year:04d}-{month:02d}-{day:02d}")
        break

    except ValueError:
        pass
