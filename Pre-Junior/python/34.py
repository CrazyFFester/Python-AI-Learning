import re
import sys


def main() -> None:
    print(parse(input("HTML: ")))


def parse(s: str) -> str | None:
    match: re.Match[str] | None = re.search(
        r"<iframe.*?src=\"https?://(?:www\.)?youtube\.com/embed/([\w\-]+)\"", s
    )

    if match is None:
        return None

    video_id: str = match.group(1)

    return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()
