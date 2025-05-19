word = input("Enter word: ")

with open("new_file.txt" , "r") as file:
    text = file.read()

if word in text:
    count = text.count(word)
    print(f"You have success, this word is available {count} times in this text.")
else:
    print("Try again with another word!")