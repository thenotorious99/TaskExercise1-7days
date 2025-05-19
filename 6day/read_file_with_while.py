while True:
    with open("names.txt", "r") as file:
        names = file.read()

    print(names)