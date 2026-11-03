algandmed = """-3
2
5
-1
8
12
6
0
-4
3"""

with open("temperatuurid.txt", "w", encoding="utf-8") as fail:
    fail.write(algandmed)

temperatuurid = []

with open("temperatuurid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        puhastatud_rida = rida.strip()
        if puhastatud_rida:
            temperatuurid.append(int(puhastatud_rida))

mõõtmiste_arv = len(temperatuurid)
keskmine = sum(temperatuurid) / mõõtmiste_arv
kõrgeim_temp = max(temperatuurid)
madalaim_temp = min(temperatuurid)

miinuspäevad = 0
soojad_päevad = 0

for temp in temperatuurid:
    if temp < 0:
        miinuspäevad += 1
    if temp >= 5:
        soojad_päevad += 1

print(f"Mõõtmisi: {mõõtmiste_arv}")
print(f"Keskmine temperatuur: {keskmine:.1f} °C")
print(f"Kõrgeim temperatuur: {kõrgeim_temp} °C")
print(f"Madalaim temperatuur: {madalaim_temp} °C")
print(f"Miinuskraadidega päevi: {miinuspäevad}")
print(f"Vähemalt 5-kraadiseid päevi: {soojad_päevad}")