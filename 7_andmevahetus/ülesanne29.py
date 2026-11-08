algandmed = """Piim 2.50 10
Leib 1.80 15
Juust 4.20 6
Õun 1.20 20
Jogurt 0.90 12"""

with open("muuk.txt", "w", encoding="utf-8") as f:
    f.write(algandmed)

kogu_müügitulu = 0.0
suurim_tulu = -1.0
suurim_toode = ""
toodete_tulemused = []

with open("muuk.txt", "r", encoding="utf-8") as f:
    for rida in f:
        if rida.strip():
            osad = rida.split()
            toode = osad[0]
            hind = float(osad[1])
            kogus = int(osad[2])

            toote_tulu = hind * kogus
            kogu_müügitulu += toote_tulu

            toodete_tulemused.append(f"{toode}: {toote_tulu:.2f} €")

            if toote_tulu > suurim_tulu:
                suurim_tulu = toote_tulu
                suurim_toode = toode

aruanne = "Müügiaruanne\n"
for tulemus in toodete_tulemused:
    aruanne += tulemus + "\n"
aruanne += f"Kogu müügitulu: {kogu_müügitulu:.2f} €\n"
aruanne += f"Suurima müügituluga toode: {suurim_toode} ({suurim_tulu:.2f} €)\n"

with open("muugiaruanne.txt", "w", encoding="utf-8") as f:
    f.write(aruanne)

print("Müügiaruanne on edukalt koostatud ja salvestatud faili 'muugiaruanne.txt'.")