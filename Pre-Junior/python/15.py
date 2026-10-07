class NegativeNumeratorException(Exception):
    def __init__(self, numerator):
        self.numerator = numerator

        super().__init__(f"ERROR: Negative numerator: {numerator}")


class ZeroDenominatorException(Exception):
    def __init__(self, denominator):
        self.denominator = denominator

        super().__init__(f"ERROR: Zero denominator: {denominator}")

numerator = 0
denominator = 0

try:
    user_input = input("Fraction: ")
    numerator_text, denominator_text = user_input.split("/")

    if not(numerator_text.isnumeric()) and not(numerator_text.isnumeric()):
        print("Hello World")
        raise ValueError("ERROR: used wrong format (1/1)")

    numerator = int(numerator_text)
    denominator = int(denominator_text)

    if numerator < 0:
        raise NegativeNumeratorException(numerator)
    if denominator == 0:
        raise ZeroDenominatorException(denominator)
except (NegativeNumeratorException, ZeroDenominatorException) as error:
    print(error)
except ValueError as error:
    print(error)
else:
    fraction = numerator / denominator

    if fraction <= 0.01:
        print("E")
    elif fraction >= 0.99:
        print("F")
    else:
        print(f"{int(fraction * 100)}%")
