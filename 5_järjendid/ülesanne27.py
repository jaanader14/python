linnad_tekst = """Tartu
Tallinn
Pärnu
Narva
Viljandi
Rakvere
Haapsalu"""

with open("linnad.txt", "w", encoding="utf-8") as fail:
    fail.write(linnad_tekst)

linnade_arv = 0

print("Failis olevad linnad:")

with open("linnad.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        puhastatud_linn = rida.strip()
        
        if puhastatud_linn:
            print(puhastatud_linn)
            linnade_arv += 1

print(f"Kokku leiti failist {linnade_arv} linna.")
