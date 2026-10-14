kuu = int(input("Sisesta kuu: "))
päev = int(input("Sisesta päev: "))
if kuu == 1 or kuu == 3 or kuu == 5 or kuu == 7 or kuu == 9 or kuu == 11 and päev <= 31:
    print("Kuupäev korrektne")

if kuu == 4 or kuu == 6 or kuu == 8 or kuu == 10 or kuu == 12 and päev <= 30:
    print("Kuupäev korrektne")

if kuu == 2 and päev <= 28:
    print("Kuupäev korrektne")
else:
    print("Sellist kuupäeva ei ole")