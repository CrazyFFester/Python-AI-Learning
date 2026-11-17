import re


def main() -> None:
    print(count(input("Text: ")))


def count(s: str) -> int:
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
