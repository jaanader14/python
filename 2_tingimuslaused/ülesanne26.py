kuu = int(input("Sisesta kuu: "))
päev = int(input("Sisesta päev: "))
if 1 <= kuu <= 12 and päev >= 1:
    
    if kuu in [1, 3, 5, 7, 8, 10, 12] and päev <= 31:
        print("Kuupäev korrektne")

    elif kuu in [4, 6, 9, 11] and päev <= 30:
        print("Kuupäev korrektne")
    
    elif kuu == 2 and päev <= 28:
        print("Kuupäev korrektne")

    else:
        print("Sellist kuupäeva ei ole.")
else:
    print("Sellist kuupäeva ei ole")