with open("ostunimekiri.txt", "w", encoding="utf-8") as fail:
    print("Sisesta toodete nimed. Lõpetamiseks kirjuta 'STOP'.\n")
    
    while True:
        toode = input("Sisesta toode: ").strip()

        if toode.upper() == "STOP":
            break

        if toode:
            fail.write(toode + "\n")

print("\nOstunimekiri salvestatud.")