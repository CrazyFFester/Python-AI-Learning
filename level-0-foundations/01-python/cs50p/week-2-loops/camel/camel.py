user_input = input()

for index, char in enumerate(user_input):
    if char.isupper() and index != 0:
        print(f"_{char.lower()}", end='')
    else:
        print(char.lower(), end='')
print()        