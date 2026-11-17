import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        tries = 0
        x, y = generate_integer(level), generate_integer(level)

        while tries < 3:
            print(f"{x} + {y} = ", end="")

            try:
                if int(input()) == x + y:
                    score += 1
                    break
            except ValueError:
                pass

            print("EEE")
            tries += 1

        if tries == 3:
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level not in [1, 2, 3]:
            continue

        return level


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Wrong level")
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level - 1), 10 ** level - 1)


if __name__ == "__main__":
    main()
