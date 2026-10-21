import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_digit_index = next((i for i, c in enumerate(s) if c.isdigit()), None)

    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if first_digit_index is not None:
                if s[first_digit_index] == "0":
                    return False
                for i in range(first_digit_index + 1, len(s)):
                    if not (s[i].isdigit()):
                        return False
            if not (any(char.isspace() for char in s)) and not (
                any(char in string.punctuation for char in s)
            ):
                return True
    return False


main()
