user_input = input()
x = int(user_input[0])
y = user_input[2]
z = int(user_input[4])

if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '/':
    print(x / z)