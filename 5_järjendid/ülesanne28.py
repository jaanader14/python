arvud_tekst = """15
8
23
42
17
9
31"""

with open("arvud.txt", "w", encoding="utf-8") as fail:
    fail.write(arvud_tekst)

arvude_arv = 0
arvude_summa = 0

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        puhastatud_rida = rida.strip()

        if puhastatud_rida:
            arv = int(puhastatud_rida)

            arvude_summa += arv
            arvude_arv += 1

print(f"Arvude arv: {arvude_arv}")
print(f"Arvude summa: {arvude_summa}")