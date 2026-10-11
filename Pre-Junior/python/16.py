items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        user_input = input("Item: ")
        user_input = user_input.title()

        if user_input in items.keys():
            cost_of_item = items[user_input]
            total += cost_of_item
        else:
            raise ValueError("ERROR: Item is not in list")
    except EOFError:
        print(f"Total: ${total:.2f}")
    except ValueError as error:
        print(error)



