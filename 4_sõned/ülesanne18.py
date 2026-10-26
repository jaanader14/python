lause = input("Sisesta lause: ")
täishäälikud = "aeiouõäöü"
loendus = {täht: 0 for täht in täishäälikud}
kokku = 0
for täht in lause.lower():
    if täht in loendus:
        loendus[täht] += 1
        kokku += 1
print(f"Täishäälikuid kokku: {kokku}")
for täht, arv in loendus.items():
    if arv > 0:
        print(f"{täht}: {arv}")