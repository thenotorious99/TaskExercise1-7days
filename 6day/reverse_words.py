with open("user_info.txt", "r") as file:
    rev_text = file.read()

print(rev_text[::-1])