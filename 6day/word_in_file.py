def word_in_text():
    word = input("Enter word: ")

    with open("user_info.txt", "r") as file:
        word_file = file.read()

        if word in word_file:
            print(f"You have success! {word} is available in text.")
        else:
            print("Try again!")


word_in_text()