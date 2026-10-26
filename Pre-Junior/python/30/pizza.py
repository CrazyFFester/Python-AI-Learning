from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename: str = sys.argv[1]
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(filename) as file:
        table = csv.reader(file)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File doesn't exist")
