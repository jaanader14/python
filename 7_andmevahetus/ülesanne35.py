import string
from collections import Counter


def analüüsi_teksti():
    failinimi = input("Sisestage analüüsitava tekstifaili nimi: ")

    try:
        with open(failinimi, "r", encoding="utf-8") as f:
            tekst = f.read()
    except FileNotFoundError:
        print(f"Viga: Faili nimega '{failinimi}' ei leitud.")
        return

    lausete_arv = tekst.count(".") + tekst.count("?") + tekst.count("!")

    if lausete_arv == 0 and tekst.strip():
        lausete_arv = 1

    puhastatud_tekst = ""
    for sümbol in tekst:
        if sümbol not in string.punctuation + "„“«»–—":
            puhastatud_tekst += sümbol
        else:
            puhastatud_tekst += (
                " "
            )

    sõnad = puhastatud_tekst.lower().split()
    sõnade_arv = len(sõnad)

    if sõnade_arv == 0:
        tulemus = (
            "Fail on tühi või ei sisalda sõnu.\n"
            f"Lausete ligikaudne arv: {lausete_arv}\n"
        )
    else:
        pikim_sõna = max(sõnad, key=len)

        sagedus = Counter(sõnad)
        sagedasemad_5 = sagedus.most_common(5)

        tulemus = (
            f"Teksti analüüsi tulemused:\n"
            f"Sõnade arv: {sõnade_arv}\n"
            f"Lausete ligikaudne arv: {lausete_arv}\n"
            f"Pikim sõna: '{pikim_sõna}' ({len(pikim_sõna)} tähte)\n"
            f"\nViis kõige sagedamat sõna:\n"
        )

        for järjekord, (sõna, arv) in enumerate(sagedasemad_5, 1):
            tulemus += f"{järjekord}. '{sõna}' – {arv} korda\n"

    tulemus_fail = "tekstanaluus.txt"
    with open(tulemus_fail, "w", encoding="utf-8") as f:
        f.write(tulemus)

    print(tulemus)
    print(f"Tulemused on edukalt salvestatud faili: {tulemus_fail}")


if __name__ == "__main__":
    analüüsi_teksti()