arvud_list = []

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        puhastatud_rida = rida.strip()
        if puhastatud_rida:
            arvud_list.append(int(puhastatud_rida))

print(f"Algne järjend failist: {arvud_list}")

suurim_arv = max(arvud_list)
vaikseim_arv = min(arvud_list)

keskmine = sum(arvud_list) / len(arvud_list)

kasvav_jarjekord = sorted(arvud_list)

print(f"Suurim arv: {suurim_arv}")
print(f"Väikseim arv: {vaikseim_arv}")
print(f"Arvude keskmine: {keskmine:.2f}")
print(f"Arvud kasvavas järjekorras: {kasvav_jarjekord}")