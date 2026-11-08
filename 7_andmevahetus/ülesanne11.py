import string

pikim_sona = ""

with open("tekst.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        sonad_real = rida.split()
        
        for sona in sonad_real:
            puhas_sona = sona.strip(string.punctuation)
            
            if len(puhas_sona) > len(pikim_sona):
                pikim_sona = puhas_sona

print(f"Kõige pikem sõna: {pikim_sona}")
print(f"Sõna pikkus: {len(pikim_sona)} tähte.")