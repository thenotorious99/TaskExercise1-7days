a = int(input("First side: "))
b = int(input("Second side: "))
c = int(input("Third side: "))

if a + b > c and a + c > b and b + c > a:
    print("We can create a triangle.")
else:
    print("We cannot create a triangle.")