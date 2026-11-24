answer = input("What is the Answer to the Great Question? ").strip().lower()

if answer in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")
