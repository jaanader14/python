temperatuur = int(input("Sisesta temperatuur: "))
if temperatuur > 24:
    print("Hoiatus!")
else:
    if temperatuur >= 18:
        print("Temperatuur on normaalne.")
    else:
        print("Hoiatus!")