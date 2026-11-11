esimene_arv = int(input("Sisesta esimene arv: "))
tehe = input("Sisesta tehe (+, -, *, /): ")
teine_arv = int(input("Sisesta teine arv: "))
if tehe == "+":
    print("Tulemus: " + str(esimene_arv + teine_arv))
elif tehe == "-":
    print("Tulemus: " + str(esimene_arv - teine_arv))
elif tehe == "*":
    print("Tulemus: " + str(esimene_arv * teine_arv))
elif tehe == "/":
    if teine_arv == 0:
        print("Nulliga ei saa jagada!")
    else:
        print("Tulemus: " + str(esimene_arv / teine_arv))
else:
    print("Tundmatu tehe.")