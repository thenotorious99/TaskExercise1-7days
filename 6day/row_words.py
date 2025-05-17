with open("user_info.txt", "r") as file:
    words = file.read().split()

print(len(words))