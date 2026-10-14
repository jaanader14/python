kasutajanimi = input("Sisesta kasutajanimi: ")
if kasutajanimi == "admin":
    parool = input("Sisesta parool: ")
    if parool == "python123":
        print("Tere tulemast!")
    else:
        print("Vale parool.")
else:
    print("Tundmatu kasutaja.")