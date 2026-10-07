def main():
    time = input()
    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")
    else:
        print("nothing. work!")


def convert(time):
    hours, minute = time.split(":")
    new_time = int(hours) + (int(minute) / 60)

    return new_time


if __name__ == "__main__":
    main()