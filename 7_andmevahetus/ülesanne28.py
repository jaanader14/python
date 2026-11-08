algandmed = """Esmaspäev 12
Teisipäev 15
Kolmapäev 11
Neljapäev 17
Reede 14
Laupäev 19
Pühapäev 16"""

with open("temperatuurid.txt", "w", encoding="utf-8") as f:
    f.write(algandmed)

temperatuurid = []
päevad = []

with open("temperatuurid.txt", "r", encoding="utf-8") as f:
    for rida in f:
        if rida.strip():
            päev, temp_str = rida.split()
            päevad.append(päev)
            temperatuurid.append(int(temp_str))

keskmine = sum(temperatuurid) / len(temperatuurid)

max_temp = max(temperatuurid)
max_päev = päevad[temperatuurid.index(max_temp)]

min_temp = min(temperatuurid)
min_päev = päevad[temperatuurid.index(min_temp)]

yle_15 = sum(1 for t in temperatuurid if t > 15)

aruanne = f"""Temperatuuride analüüs
Nädala keskmine temperatuur: {keskmine:.1f} °C
Kõige soojem päev: {max_päev} ({max_temp} °C)
Kõige külmem päev: {min_päev} ({min_temp} °C)
Päevi üle 15 kraadi: {yle_15}"""

with open("temperatuuri_aruanne.txt", "w", encoding="utf-8") as f:
    f.write(aruanne)

print("Analüüs on edukalt lõpetatud ja tulemused salvestatud faili 'temperatuuri_aruanne.txt'.")