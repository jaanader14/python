isikukood = (input("Sisesta isikukood: "))

if len(isikukood) == 11 and isikukood.isdigit() and "1" <= isikukood[0] <= "8":
    print("Vorming on sobiv")
else:
    print("Vorming ei sobi")