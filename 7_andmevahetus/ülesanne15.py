nimi = input("Sisesta oma nimi: ").strip()
vanus = input("Sisesta oma vanus: ").strip()
email = input("Sisesta oma e-posti aadress: ").strip()

with open("kasutaja.txt", "w", encoding="utf-8") as fail_kirjutamiseks:
    fail_kirjutamiseks.write(nimi + "\n")
    fail_kirjutamiseks.write(vanus + "\n")
    fail_kirjutamiseks.write(email + "\n")

print("\nAndmed on edukalt salvestatud faili kasutaja.txt!\n")

with open("kasutaja.txt", "r", encoding="utf-8") as fail_lugemiseks:
    sisu = fail_lugemiseks.read()
    print(sisu)