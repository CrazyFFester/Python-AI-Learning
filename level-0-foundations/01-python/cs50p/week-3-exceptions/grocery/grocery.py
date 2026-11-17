grocery_list = {}

while True:
    try:
        user_input = input().upper()

        if user_input in grocery_list.keys():
            grocery_list[user_input] += 1
        else:
            grocery_list[user_input] = 1
    except EOFError:
        for k, v in grocery_list.items():
            print(f"{v} {k}")
        break
