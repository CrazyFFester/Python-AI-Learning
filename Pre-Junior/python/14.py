import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if s[-1].isalpha() and not(s[-1].isnumeric()):
                if not(any(char.isspace() for char in s)) and \
                    not(any(char in string.punctuation for char in s)):
                    return True
    return False



main()
