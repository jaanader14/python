kasutajanimi = input("Kasutajanimi: ")

if not (5 <= len(kasutajanimi) <= 15):
    print("Viga: kasutajanimi peab olema 5-15 tähemärki.")

elif not kasutajanimi[0].isalpha():
    print("Viga: kasutajanimi peab algama tähega.")

elif not kasutajanimi.isalnum() or not kasutajanimi.isascii():
    print("Viga: kasutajanimi tohib sisaldada ainult ladina tähti ja numbreid.")

else:
    print("Kasutajanimi sobib.")