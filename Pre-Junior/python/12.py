due = 50
change = 0

while due > 0:
    print(f"Amount Due: {due}")

    coin = int(input("Insert Coin: "))

    if coin in (25, 10, 5):
        due -= coin

change = -due 

print(f"Change Owed: {change}")