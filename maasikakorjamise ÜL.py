def raha_eurodes(maasikakastide_arv, kilo_hind_sentides):
    eurod = maasikakastide_arv * 5 * (kilo_hind_sentides / 100)
    return round(eurod, 1)

failinimi = input("Sisetage faili nimi: ")
hind_sentides = int(input("Sisestage kilo hind sentides: "))
kokku_raha = 0.0
päeva_loendur = 1

try:
    with open(failinimi, "r", encoding="utf-8") as fail:
        for rida in fail:
            rida = rida.strip()
            if rida:
                kastide_arv = int(rida)
                päeva_raha = raha_eurodes(kastide_arv, hind_sentides)
                print(f"{päeva_loendur}. päeval sai {päeva_raha} eurot.")

                kokku_raha += päeva_raha
                päeva_loendur += 1
    print(f"Kokku sai: {round(kokku_raha, 1)} eurot.")
except FileNotFoundError:
    print("Viga: Faili nimega " + failinimi + " ei leitud.")