max_num = None

for i in range(5):
    num = int(input("Enter number: "))
    if max_num is None or num > max_num:
        max_num = num

print(f"The biggest numer is: {max_num}")
