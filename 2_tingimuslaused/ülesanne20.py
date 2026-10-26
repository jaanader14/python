kolmnurgakülg1 = int(input("Sisesta kolmnurga esimese külje pikkus: "))
kolmnurgakülg2 = int(input("Sisesta kolmnurga teise külje pikkus: "))
kolmnurgakülg3 = int(input("Sisesta kolmnurga kolmanda külje pikkus: "))
if (kolmnurgakülg1 + kolmnurgakülg2 > kolmnurgakülg3) and (kolmnurgakülg1 + kolmnurgakülg3 > kolmnurgakülg2) and (kolmnurgakülg2 + kolmnurgakülg3 > kolmnurgakülg1):
    print("Kolmnurk on võimalik.")
else:
    print("Kolmnurk ei ole võimalik.")