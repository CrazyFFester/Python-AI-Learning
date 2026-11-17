def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError) as error:
            print(error)
        else:
            print(gauge(percentage))
            break


def convert(fraction):
    numerator_text, denominator_text = fraction.split("/")

    numerator = int(numerator_text)
    denominator = int(denominator_text)

    if denominator == 0:
        raise ZeroDivisionError("ERROR: denominator equals 0")
    if numerator < 0:
        raise ValueError("ERROR: negative numerator")
    if numerator > denominator:
        raise ValueError("ERROR: numerator greater than denominator")

    percentage = numerator / denominator * 100

    return round(percentage)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
