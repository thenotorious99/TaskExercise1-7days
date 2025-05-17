# s purvata comanda otvarqm purviq file, a s vtorata go copiram s operatora "a"
with open("user_info.txt", "r") as firstfile, open("second.txt", "a") as secondfile:
    # S for cikul minavam prez celiq text i kopiram faila v drugiq
    for line in firstfile:
        secondfile.write(line)