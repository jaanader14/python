with open("nimed.txt", "w", encoding="utf-8") as fail_kirjutamiseks:
    nimed_list = ["Mari", "Jüri", "Anna", "Peeter", "Kati", "Martin"]
    for nimi in nimed_list:
        fail_kirjutamiseks.write(nimi + "\n")

ridade_arv = 0

with open("nimed.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        if rida.strip():
            ridade_arv += 1

print(f"Failis on {ridade_arv} nime.")