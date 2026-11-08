def arvude_tootlus():
    arvud = []
    for i in range(5):
        while True:
            try:
                arv = int(input(f"Sisesta {i+1}. täisarv: "))
                arvud.append(arv)
                break
            except ValueError:
                print("Viga! Palun sisesta korrektne täisarv.")

    with open("sisestatud_arvud.txt", "w", encoding="utf-8") as fail:
        for arv in arvud:
            fail.write(str(arv) + "\n")
            
    print("\nAndmed edukalt faili salvestatud.\n")

    loetud_arvud = []
    with open("sisestatud_arvud.txt", "r", encoding="utf-8") as fail:
        for rida in fail:
            loetud_arvud.append(int(rida.strip()))

    summa = sum(loetud_arvud)
    keskmine = summa / len(loetud_arvud)

    arvude_tekst = ", ".join(map(str, loetud_arvud))
    print(f"Sisestatud arvud: {arvude_tekst}")
    print(f"Summa: {summa}")
    print(f"Keskmine: {keskmine}")

arvude_tootlus()