import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with (
        open(sys.argv[1]) as source,
        open(sys.argv[2], "w", newline="") as target,
    ):
        reader = csv.DictReader(source)

        writer = csv.DictWriter(target, fieldnames=["first", "last", "house"])

        writer.writeheader()

        for row in reader:
            first, last = row["name"].split(", ")
            house = row["house"]
            writer.writerow(
                {
                    "first",
                }
            )
except (FileExistsError, IsADirectoryError):
    print("Could not read ")
