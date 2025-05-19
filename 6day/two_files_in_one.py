with open("user_info.txt", "r") as firstfile, open("second.txt", "r") as secondfile, open("new_file.txt", "a") as thirdfile:
    thirdfile.writelines(firstfile.readlines())
    thirdfile.writelines(secondfile.readlines())