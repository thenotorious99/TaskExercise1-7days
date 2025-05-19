with open("numbers.txt", "r") as firstfile, open("numbers2.txt", "a") as secondfile:
    for line in firstfile:
        # strip premahva skriti simvoli kato \n
        line = line.strip()
        # isdigit predpazva ot greshki ako ima nechislovi redove
        if line.isdigit() and int(line) % 2 == 0:
            secondfile.write(line + "\n")