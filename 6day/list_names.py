names = ["Ivan", "Peter", "Joro", "Bobi", "Georgi",
         "Monika", "Dimitur", "Lubomir", "Stefano", "Mario"]

with open("names.txt", "w") as file:
    for i in names:
        file.write(i + "\n")

