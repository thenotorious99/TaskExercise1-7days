num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter some operator (+, -, *, /): ")

if operation == "+":
    print(f"The result is: {num1 + num2}")
elif operation == "-":
    print(f"The results is: {num1 - num2}")
elif operation == "*":
    print(f"The results is: {num1 * num2}")
elif operation == "/":
    print(f"The results is: {num1 / num2}")
else:
    print("Invalid operation.")


