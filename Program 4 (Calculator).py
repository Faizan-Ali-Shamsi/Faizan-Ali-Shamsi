print("Select operation.")

print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. quit")

choice = input("1/2/3/4/5: ")

if choice == 5:
    print("you wasted my time.")

elif choice in ("1", "2", "3", "4"):

    a = float(input("first number : "))
    b = float(input("second number : "))

    if choice == "1":
        result = a + b
        print(f"{a} + {b} = {result}")

    elif choice == "2":
        result = a - b
        print(f"{a} - {b} = {result}")

    elif choice == "3":
        result = a * b
        print(f"{a} * {b} = {result}")

    elif choice == "4":
        if b == 0:
            print("my math isn't mathing")
        else:
            result = a / b
            print(f"{a} / {b} = {result}")
else:
    print("Input numbers you illiterate whore.")