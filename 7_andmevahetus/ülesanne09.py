with open("arvud.txt", "w", encoding="utf-8") as fail_kirjutamiseks:
    naidis_arvud = [12, 4, 25, 32, 8, 18]
    for arv in naidis_arvud:
        fail_kirjutamiseks.write(f"{arv}\n")

arvude_list = []

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        puhas_rida = rida.strip()
        if puhas_rida:
            arvude_list.append(int(puhas_rida))

if arvude_list:
    suurim = max(arvude_list)
    vaikseim = min(arvude_list)
    vahe = suurim - vaikseim

    print(f"Suurim arv: {suurim}")
    print(f"Väikseim arv: {vaikseim}")
    print(f"Vahe: {vahe}")
else:
    print("Fail on tühi või ei sisalda sobivaid arve.")