def two_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > num2:
        return f"The bigger number is: {num1}"
    elif num2 > num1:
        return f"The bigger number is: {num2}"
    else:
        return f"Try again"

print(two_numbers())