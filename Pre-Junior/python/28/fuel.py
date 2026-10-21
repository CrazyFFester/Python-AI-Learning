import fractions


class NegativeNumeratorException(Exception):
    def __init__(self, numerator):
        self.numerator = numerator

        super().__init__(f"ERROR: Negative numerator: {numerator}")


class ZeroDenominatorException(Exception):
    def __init__(self, denominator):
        self.denominator = denominator

        super().__init__(f"ERROR: Zero denominator: {denominator}")


def main():
    numerator = 0
    denominator = 0

    try:
        fraction = input("Fraction: ")
        covert(fraction)
    except (NegativeNumeratorException, ZeroDenominatorException) as error:
        print(error)
    except ValueError as error:
        print(error)
    else:
        percentage = numerator / denominator * 100

        gauge(percentage)


def covert(fraction):
    numerator_text, denominator_text = fraction.split("/")

    if not (numerator_text.isnumeric()) and not (numerator_text.isnumeric()):
        print("Hello World")
        raise ValueError("ERROR: used wrong format (1/1)")

    numerator = int(numerator_text)
    denominator = int(denominator_text)

    if numerator < 0:
        raise NegativeNumeratorException(numerator)
    if denominator == 0:
        raise ZeroDenominatorException(denominator)


def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{int(percentage * 100)}%")


if __name__ == "__main__":
    main()
