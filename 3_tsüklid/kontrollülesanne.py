summa = 0
loendur = 0
positiivsed = 0
negatiivsed = 0
paarisarvud = 0
paaritud = 0
arv = int(input("Sisesta arv: "))
while arv != 0:
    summa += arv
    loendur += 1

    if arv > 0:
        positiivsed += 1
    elif arv < 0:
        negatiivsed += 1

    if arv % 2 == 0:
        paarisarvud += 1
    else:
        paaritud += 1

    arv = int(input("Sisesta arv: "))

if loendur == 0:
    print("Ühtegi arvu ei sisestatud.")
else:
    keskmine = summa / loendur
    print("--- TULEMUSED ---")
    print(f"Sisestatud arve: {loendur}")
    print(f"Summa: {summa}")
    print(f"Keskmine: {keskmine}")
    print(f"Positiivseid arve: {positiivsed}")
    print(f"Negatiivseid arve: {negatiivsed}")
    print(f"Paarisarve: {paarisarvud}")
    print(f"Paarituid arve: {paaritud}")