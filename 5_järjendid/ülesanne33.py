hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]
hinnete_koguarv = len(hinded)
keskmine = sum(hinded) / hinnete_koguarv
sagedasem_hinne = max(hinded, key=hinded.count)
positiivsed_hinded = 0
mitterahuldavad_hinded = 0

for hinne in hinded:
    if hinne > 2:
        positiivsed_hinded += 1

for hinne in hinded:
    if hinne <= 2:
        mitterahuldavad_hinded += 1

print(f"Hinnete koguarv: {hinnete_koguarv}")
print(f"Kekmine hinne: {keskmine:.2f}")
print(f"Kõige sagedasem hinne: {sagedasem_hinne}")
print(f"Positiivsete hinnete arv: {positiivsed_hinded}")
print(f"Negatiivsete hinnete arv: {mitterahuldavad_hinded}")
print("Hinnete esinemiste arv:")

for hinne in sorted(set(hinded)):
    arv = hinded.count(hinne)
    print(f"Hinne {hinne}: esineb {arv} korda")