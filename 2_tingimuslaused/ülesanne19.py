esimene_arv = int(input("Sisesta esimene arv: "))
teine_arv = int(input("Sisesta teine arv: "))
kolmas_arv = int(input("Sisesta kolmas arv: "))
if esimene_arv > teine_arv and esimene_arv > kolmas_arv:
    print("Suurim arv on: " + str(esimene_arv))

if teine_arv > esimene_arv and teine_arv > kolmas_arv:
    print("Suurim arv on: " + str(teine_arv))

if kolmas_arv > esimene_arv and kolmas_arv > teine_arv:
    print("Suurim arv on: " + str(kolmas_arv))
