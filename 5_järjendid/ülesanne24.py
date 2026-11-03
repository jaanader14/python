laused = ["Täna õpime Pythonit", "Järjendid on väga kasulikud", "Programmeerimine nõuab harjutamist", "Tartu on ilus linn"]
kogu_a_arv = 0
kõige_pikem_lause = ""

print("Lausete analüüs:")

for lause in laused:
    pikkus = len(lause)
    a_lause = lause.lower().count("a")
    kogu_a_arv += a_lause
    if len(lause) > len(kõige_pikem_lause):
        kõige_pikem_lause = lause

    print(f"Lause: '{lause}'")
    print(f"  - Tähemärkide arv: {pikkus}")
    print(f"  - 'a' tähti lauses: {a_lause}")
    print()

print(f"Täht 'a' esineb kõikide lausete peale kokku {kogu_a_arv} korda.")
print(f"Kõige pikem lause on: '{kõige_pikem_lause}'")