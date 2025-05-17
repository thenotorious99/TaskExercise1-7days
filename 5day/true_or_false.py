def even_num():
    num = int(input("Enter number: "))
    if num % 2 == 0:
        return True
    else:
        return False
print(even_num())