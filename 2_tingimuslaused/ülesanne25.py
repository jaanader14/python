esimene_arv = int(input("Sisesta esimene arv: "))
tehe = input("Sisesta tehe (+, -, *, /): ")
teine_arv = int(input("Sisesta teine arv: "))
if tehe == "+":
    print("Tulemus: " + str(esimene_arv + teine_arv))
if tehe == "-":
    print("Tulemus: " + str(esimene_arv - teine_arv))
if tehe == "*":
    print("Tulemus: " + str(esimene_arv * teine_arv))
if tehe == "/":
    print("Tulemus: " + str(esimene_arv / teine_arv))