import random


level = 0

while True:
    user_input = input("Level: ")

    if user_input.isnumeric() and int(user_input) > 0:
        number = int(user_input)

        break

level_range = random.randrange(1, level)

while True:
    user_input = input("Level: ")

    if not(user_input.isnumeric()) or int(user_input) <= 0:
        if 

        break
