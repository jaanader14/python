with open("arvud.txt", "w", encoding="utf-8") as fail_kirjutamiseks:
    naidis_arvud = [12, 7, 24, 5, 8, 10]
    for arv in naidis_arvud:
        fail_kirjutamiseks.write(f"{arv}\n")

paaris_loendur = 0
paaritu_loendur = 0

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        puhas_rida = rida.strip()

        if puhas_rida:
            arv = int(puhas_rida)

            if arv % 2 == 0:
                paaris_loendur += 1
            else:
                paaritu_loendur += 1

print(f"Paarisarve: {paaris_loendur}")
print(f"Paarituid arve: {paaritu_loendur}")