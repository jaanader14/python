nimed = []
punktid = []
with open("kontrolltoo.csv", "r", encoding="utf-8") as fail:
    for rida in fail:
        puhastatud_rida = rida.strip()
        if puhastatud_rida:
            nimi, punktisumma = puhastatud_rida.split(";")
            nimed.append(nimi)
            punktid.append(int(punktisumma))

print("KONTROLLTÖÖ TULEMUSED")
for i in range(len(nimed)):
    print(f"{i + 1}. {nimed[i]} – {punktid[i]} punkti")
print()

print("ÕPILASED JA HINDED")
for i in range(len(nimed)):
    if 90 <= punktid[i] <= 100:
        hinne = 5
    elif 75 <= punktid[i] <= 89:
        hinne = 4
    elif 50 <= punktid[i] <= 74:
        hinne = 3
    elif 20 <= punktid[i] <= 49:
        hinne = 2
    else:
        hinne = 1

    print(f"{nimed[i]} – {punktid[i]} punkti – hinne {hinne}")
print()

õpilasi_kokku = len(nimed)
keskmine = sum(punktid) / õpilasi_kokku

parim_skoor = max(punktid)
halvim_skoor = min(punktid)

parimad_õpilased = []
halvimad_õpilased = []

for i in range(õpilasi_kokku):
    if punktid[i] == parim_skoor:
        parimad_õpilased.append(nimed[i])
    if punktid[i] == halvim_skoor:
        halvimad_õpilased.append(nimed[i])

parimad_saavutused = ", ".join(parimad_õpilased)
halvimad_saavutused = ", ".join(halvimad_õpilased)

sooritas = 0
ei_sooritanud = 0

for skoor in punktid:
    if skoor >= 50:
        sooritas += 1
    else:
        ei_sooritanud += 1

print("KONTROLLTÖÖ STATISTIKA")
print(f"Õpilasi kokku: {õpilasi_kokku}")
print(f"Keskmine punktisumma: {keskmine:.1f}")
print(f"Parim tulemus: {parimad_saavutused} – {parim_skoor} punkti")
print(f"Madalaim tulemus: {halvimad_saavutused} – {halvim_skoor} punkti")
print(f"Kontrolltöö sooritas: {sooritas} õpilast")
print(f"Kontrolltööd ei sooritanud: {ei_sooritanud} õpilast")
print()

print("ÕPILASE OTSIMINE")
otsitav_nimi = input("Sisesta õpilase nimi: ").strip().lower()

leitud = False

for i in range(õpilasi_kokku):
    if nimed[i].lower() == otsitav_nimi:
        if 90 <= punktid[i] <= 100:
            hinne = 5
        elif 75 <= punktid[i] <= 89:
            hinne = 4
        elif 50 <= punktid[i] <= 74:
            hinne = 3
        elif 20 <= punktid[i] <= 49:
            hinne = 2
        else:
            hinne = 1
        print(f"Õpilane: {nimed[i]}")
        print(f"Punktid: {punktid[i]}")
        print(f"Hinne: {hinne}")
        leitud = True
        break

if not leitud:
    print("Sellist õpilast ei leitud.")