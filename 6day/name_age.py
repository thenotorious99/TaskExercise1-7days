name = (input("Enter your name: "))
age = int(input("Enter your age: "))

with open("user_info.txt", 'w') as file:
    file.write(f"Name: {name}" + "\n")
    file.write(f"Age: {age}")
