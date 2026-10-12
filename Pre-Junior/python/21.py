import inflect


words = []
p = inflect.engine()

while True:
    try:
        user_input = input("Name: ")
        words.append(user_input)
    except EOFError:
        print()
        break

output = p.join(words)

print(f"Adieu, adieu, to {output}")
