total = 0
with open("numbers.txt", "r") as file:
    for i in file:
        total += int(i.strip())
print(f"Total sum: {total}")