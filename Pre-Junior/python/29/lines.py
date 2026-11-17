import sys


def is_code_line(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename: str = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            print(sum(1 for line in file if is_code_line(line)))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
