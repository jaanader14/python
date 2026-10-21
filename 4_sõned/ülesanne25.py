isikukood = int(input("Sisesta isikukood:"))
pikkus = len(isikukood)
if isikukood[0] >= 1 and isikukood <= 8 and pikkus == 11:
    print("Vorming on sobiv")
else:
    print("Vorming ei sobi")