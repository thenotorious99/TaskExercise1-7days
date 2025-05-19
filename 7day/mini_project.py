def mini_pro():
    name = input("Enter your name: ")
    assessment = int(input("Enter your assessment 1 to 6: "))

    with open("mini_pro.txt", "a") as file:
        file.write(f"Name: {name}, Assessment: {assessment}" + "\n")


    with open("mini_project.py", "r") as file:
        print(file.read())

mini_pro()