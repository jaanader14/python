with open("tervitus.txt", "w", encoding="utf-8") as fail_kirjutamiseks:
    fail_kirjutamiseks.write("Tere tulemast Pythoni kursusele!\n")
    fail_kirjutamiseks.write("Täna õpime failidega töötamist.\n")
    fail_kirjutamiseks.write("Failides saab andmeid säilitada.\n")

fail_lugemiseks = open("tervitus.txt", "r", encoding="utf-8")

faili_sisu = fail_lugemiseks.read()

fail_lugemiseks.close()

print(faili_sisu)