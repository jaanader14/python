kolmnurgakülg1 = int(input("Sisesta kolmnurga esimese külje pikkus: "))
kolmnurgakülg2 = int(input("Sisesta kolmnurga teise külje pikkus: "))
kolmnurgakülg3 = int(input("Sisesta kolmnurga kolmanda külje pikkus: "))
if kolmnurgakülg1 < kolmnurgakülg2 + kolmnurgakülg3:
    print("Kolmnurk on võimalik.")
else:
    if kolmnurgakülg2 < kolmnurgakülg1 + kolmnurgakülg3:
        print("Kolmnurk on võimalik.")
    else:
        if kolmnurgakülg3 < kolmnurgakülg1 + kolmnurgakülg2:
            print("Kolmnurk on võimalik.")
        else:
            print("Kolmnurk ei ole võimalik.")