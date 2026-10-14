vanus = int(input("Sisesta vanus: "))
õpilane = input("Kas oled õpilane (jah/ei): ")
if vanus < 7:
    print("tasuta")
elif vanus >= 7 and vanus <=17:
    print("5€")
elif vanus >= 18 and õpilane == "jah":
    print("8€")
elif vanus >=65:
    print("6€")
else:
    print("12€")