import os

FAILINIMI = "kulud.txt"


def lisa_kulu():
    print("\n--- Uue kulu lisamine ---")
    kuupaev = input("Sisestage kuupäev (nt 12.10.2026): ")
    kategooria = input("Sisestage kategooria (nt Toit): ")
    kirjeldus = input("Sisestage kirjeldus (nt Lõunasöök): ")

    while True:
        try:
            summa = float(input("Sisestage summa (nt 8.50): "))
            break
        except ValueError:
            print("Viga: Summa peab olema number. Proovige uuesti.")

    with open(FAILINIMI, "a", encoding="utf-8") as f:
        f.write(f"{kuupaev};{kategooria};{kirjeldus};{summa:.2f}\n")

    print("Kulu on edukalt salvestatud!")


def loe_kulud():
    if not os.path.exists(FAILINIMI):
        return []

    kulud = []
    with open(FAILINIMI, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if rida:
                osad = rida.split(";")
                if len(osad) == 4:
                    kulud.append(
                        {
                            "kuupaev": osad[0],
                            "kategooria": osad[1],
                            "kirjeldus": osad[2],
                            "summa": float(osad[3]),
                        }
                    )
    return kulud


def kuva_koik_kulud():
    kulud = loe_kulud()
    if not kulud:
        print("\nKulude fail on tühi või seda ei eksisteeri veel.")
        return

    print("\n--- Kõik salvestatud kulud ---")
    for kulu in kulud:
        print(
            f"{kulu['kuupaev']} | {kulu['kategooria']:<12} | {kulu['kirjeldus']:<15} | {kulu['summa']:.2f} €"
        )


def arvuta_kogukulu():
    kulud = loe_kulud()
    kogusumma = sum(kulu["summa"] for kulu in kulud)
    print(f"\nKogukulu kokku: {kogusumma:.2f} €")
    return kogusumma


def kuva_kategooria_kulud():
    kulud = loe_kulud()
    if not kulud:
        print("\nKulude fail on tühi.")
        return

    otsitav = input("\nSisestage kategooria, mida soovite kuvada: ").strip()
    leitud = [
        k for k in kulud if k["kategooria"].lower() == otsitav.lower()
    ]

    if not leitud:
        print(f"Kategooriast '{otsitav}' kulusid ei leitud.")
        return

    print(f"\n--- Kulud kategoorias: {leitud[0]['kategooria']} ---")
    kategooria_summa = 0
    for kulu in leitud:
        print(
            f"{kulu['kuupaev']} | {kulu['kirjeldus']:<15} | {kulu['summa']:.2f} €"
        )
        kategooria_summa += kulu["summa"]
    print(f"Kategooria kogukulu: {kategooria_summa:.2f} €")


def salvesta_kokkuvote():
    kulud = loe_kulud()
    if not kulud:
        print("\nPole andmeid, millest kokkuvõtet teha.")
        return

    kategooriad = {}
    kogusumma = 0
    for kulu in kulud:
        kat = kulu["kategooria"]
        summa = kulu["summa"]
        kategooriad[kat] = kategooriad.get(kat, 0) + summa
        kogusumma += summa

    kokkuvote_fail = "kulude_kokkuvote.txt"
    with open(kokkuvote_fail, "w", encoding="utf-8") as f:
        f.write("KULUDE KOKKUVÕTE\n")
        f.write("================\n")
        f.write(f"Tehingute arv kokku: {len(kulud)}\n")
        f.write(f"Kogukulu: {kogusumma:.2f} €\n\n")
        f.write("Kulud kategooriate kaupa:\n")
        f.write("-------------------------\n")
        for kat, summa in kategooriad.items():
            f.write(f"{kat}: {summa:.2f} €\n")

    print(f"\nKokkuvõte on edukalt salvestatud faili: {kokkuvote_fail}")


def peamenüü():
    while True:
        print("\n===== KULUDE ARVESTAMINE =====")
        print("1. Lisa uus kulu")
        print("2. Kuva kõik kulud")
        print("3. Arvuta kogukulu")
        print("4. Kuva valitud kategooria kulud")
        print("5. Salvesta kokkuvõte faili")
        print("6. Sulge programm")

        valik = input("Valige tegevus (1-6): ").strip()

        if valik == "1":
            lisa_kulu()
        elif valik == "2":
            kuva_koik_kulud()
        elif valik == "3":
            arvuta_kogukulu()
        elif valik == "4":
            kuva_kategooria_kulud()
        elif valik == "5":
            salvesta_kokkuvote()
        elif valik == "6":
            print("Head aega!")
            break
        else:
            print("Vigane valik! Palun vali number vahemikus 1-6.")


if __name__ == "__main__":
    peamenüü()