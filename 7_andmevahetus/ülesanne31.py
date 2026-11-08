algandmed = """Mari;mari@example.com;5551001
Jüri;jyri@example.com;5551002
Anna;anna@example.com;5551003
Peeter;peeter@example.com;5551004"""

with open("kontaktid.txt", "w", encoding="utf-8") as f:
    f.write(algandmed)

kontaktid = {}

try:
    with open("kontaktid.txt", "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if rida:
                nimi, email, telefon = rida.split(";")
                kontaktid[nimi.lower()] = {"nimi": nimi, "email": email, "telefon": telefon}
except FileNotFoundError:
    print("Viga: Faili 'kontaktid.txt' ei leitud!")
    exit()

print("--- Kontaktide otsing ---")
print("Otsingu lõpetamiseks sisesta 'lõpp' või vajuta Enter ilma midagi kirjutamata.\n")

while True:
    otsing = input("Sisesta nimi otsimiseks: ").strip()

    if otsing.lower() == "lõpp" or otsing == "":
        print("Programmi töö lõpetatud.")
        break

    voti = otsing.lower()
    if voti in kontaktid:
        tulemus = kontaktid[voti]
        print(f"Leitud kontakt: {tulemus['nimi']}")
        print(f"  E-post: {tulemus['email']}")
        print(f"  Telefon: {tulemus['telefon']}")
    else:
        print(f"Kontakti nimega '{otsing}' ei leitud.\n")