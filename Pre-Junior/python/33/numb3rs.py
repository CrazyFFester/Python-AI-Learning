import re


def main() -> None:
    print(validate(input("IPv4 Address: ")))


def validate(ipv4) -> bool:
    match = re.search(
        r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ipv4
    )

    if match is None:
        return False

    for group in match.groups():
        if len(group) > 1 and group[0] == "0":
            return False
        if int(group) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
