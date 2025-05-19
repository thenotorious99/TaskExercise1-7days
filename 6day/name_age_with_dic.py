name_age = [
    {"name": "Ivan", "age": 30},
    {"name": "Joro", "age": 32},
    {"name": "Elizabet", "age": 24},
    {"name": "Flory", "age": 17},
    {"name": "Galin", "age": 64},

]

with open("name_age.txt", "w") as file:
    for name in name_age:
        res = f"Name: {name['name']}, Years: {name['age']}" + "\n"
        file.write(res)