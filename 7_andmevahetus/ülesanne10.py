with open("tekst.txt", "w", encoding="utf-8") as fail_kirjutamiseks:
    fail_kirjutamiseks.write("Python on populaarne programmeerimiskeel.\n")
    fail_kirjutamiseks.write("Python sobib hästi algajatele.\n")
    fail_kirjutamiseks.write("Failide töötlemine on oluline oskus.\n")

sonade_arv = 0

with open("tekst.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        sonad_real = rida.split()

        sonade_arv += len(sonad_real)

print(f"Tekstis on {sonade_arv} sõna.")