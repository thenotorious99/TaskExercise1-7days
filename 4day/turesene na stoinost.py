list1 = [1, 45, 21, 3, 7, 32, 87, 12, 17, 20, 134]

for i in list1:
    number = int(input("Enter number: "))
    if number in list1:
        print(f"The success number is: {number} ")
    else:
        print("Wrong number! Try Again!")
