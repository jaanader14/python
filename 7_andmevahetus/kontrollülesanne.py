import os

def leia_hinne(keskmine):
    """Määrab hinde vastavalt hindamisskaalale."""
    if keskmine >= 90:
        return 5
    elif keskmine >= 75:
        return 4
    elif keskmine >= 60:
        return 3
    elif keskmine >= 50:
        return 2
    else:
        return 1

def tootle_tulemused():
    sisendfail = "tulemused.txt"
    valjundfail = "aruanne.txt"

    if not os.path.exists(sisendfail):
        print(f"Viga: Lähtefaili '{sisendfail}' ei leitud!")
        return

    opilased = []
    koik_keskmised = []
    positiivsed_luger = 0

    with open(sisendfail, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if not rida:
                continue

            osad = rida.split(";")
            if len(osad) < 4:
                continue

            nimi = osad[0]
            tulemused = [float(x) for x in osad[1:]]

            keskmine = sum(tulemused) / len(tulemused)
            hinne = leia_hinne(keskmine)

            if hinne >= 3:
                positiivsed_luger += 1

            koik_keskmised.append(keskmine)
            opilased.append(
                {"nimi": nimi, "keskmine": keskmine, "hinne": hinne}
            )

    if not opilased:
        print("Failis puuduvad töödeldavad andmed.")
        return

    klassi_keskmine = sum(koik_keskmised) / len(koik_keskmised)

    parim_opilane = max(opilased, key=lambda x: x["keskmine"])["nimi"]
    norgim_opilane = min(opilased, key=lambda x: x["keskmine"])["nimi"]

    aruande_tekst = "ÕPILASTE TULEMUSTE ARUANNE\n"

    for o in opilased:
        aruande_tekst += f"{o['nimi']:<10} Keskmine: {o['keskmine']:.2f}  Hinne: {o['hinne']}\n"

    aruande_tekst += f"Klassi keskmine: {klassi_keskmine:.2f}\n"
    aruande_tekst += f"Parim õpilane: {parim_opilane}\n"
    aruande_tekst += f"Nõrgim õpilane: {norgim_opilane}\n"
    aruande_tekst += f"Positiivse hindega õpilasi: {positiivsed_luger}\n"

    print(aruande_tekst)

    with open(valjundfail, "w", encoding="utf-8") as f:
        f.write(aruande_tekst)

    print(f"Aruanne on edukalt salvestatud faili: {valjundfail}")


if __name__ == "__main__":
    tootle_tulemused()