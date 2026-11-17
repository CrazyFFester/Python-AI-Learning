import random


while True:
    try:
        user_input = int(input("Level: "))
    except ValueError:
        continue

    if user_input > 0:
        level = user_input
        break

target = random.randrange(1, level+1)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess <= 0:
        continue

    if guess < target:
        print("Too small!")
    elif guess > target:
        print("Too large!")
    else:
        print("Just right!")
        break
