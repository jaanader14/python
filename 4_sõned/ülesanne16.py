kasutajanimi = input("Kasutajanimi:")
pikkus = len(kasutajanimi)
if pikkus < 5 or pikkus > 15:
    print("Viga: Kasutajanimi peab olema 5-15 tähemärki")
elif kasutajanimi:
    print("Viga: kasutajanimi peab algama tähega")
elif