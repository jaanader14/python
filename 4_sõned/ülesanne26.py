print("Kirjuta sõna:")
sõna = input()
while sõna != "head aega":
    if sõna == "tere":
        print("Tere! Kuidas saan aidata?")
    elif sõna == "nimi":
        print("Minu nimi on PyBot.")
    elif sõna == "python":
        print("Python on programmeerimiskeel.")
    elif sõna == "abi":
        print("Kirjuta tere, nimi või python.")
    else:
        print("Tundmatu sõna")
    print("Kirjuta sõna:")
    sõna = input()
print("Nägemist!")