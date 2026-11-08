algandmed = """12
18
viga
25
-4
puudub
30
15"""

with open("mootmised.txt", "w", encoding="utf-8") as f:
    f.write(algandmed)

kehtivad_arvud = []
vigased_kirjed = 0

with open("mootmised.txt", "r", encoding="utf-8") as f:
    for rida in f:
        rida = rida.strip()
        if not rida:
            continue
            
        try:
            arv = int(rida)
            kehtivad_arvud.append(arv)
        except ValueError:
            vigased_kirjed += 1

kehtivad_loendus = len(kehtivad_arvud)

if kehtivad_loendus > 0:
    keskmine = sum(kehtivad_arvud) / kehtivad_loendus
else:
    keskmine = 0.0

with open("korrektsed_mootmised.txt", "w", encoding="utf-8") as f:
    for arv in kehtivad_arvud:
        f.write(f"{arv}\n")

print("Andmete filtreerimise tulemused:")
print(f"Kehtivaid arvväärtusi: {kehtivad_loendus}")
print(f"Vigaseid kirjeid: {vigased_kirjed}")
print(f"Kehtivate väärtuste keskmine: {keskmine:.2f}")
print("\nKehtivad arvväärtused on salvestatud faili 'korrektsed_mootmised.txt'.")