parool = input("Sisesta parrol:")
if len(parool) < 8:
    print("Parooli pikkus on liiga lühike")
elif len(parool) < 12:
    print("Parooli pikkus on sobiv")
else:
    print("Pikk parool")