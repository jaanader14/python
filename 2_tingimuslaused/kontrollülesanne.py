nimi = input("Sisesta oma nimi: ")
punktisumma = int(input("Sisesta punktisumma: "))
puudumised = int(input("Sisesta puudumiste arv: "))
tööd = (input("Kas kõik tööd on esitatud (jah/ei)"))
print("Õpilane: " + nimi)
if punktisumma >= 90:
    print("Hinne: 5")
elif punktisumma >= 75:
    print("Hinne: 4")
elif punktisumma >= 50:
    print("Hinne: 3")
elif punktisumma >= 20:
    print("Hinne: 2")
elif punktisumma >= 0:
    print("Hinne: 1")

if puudumised > 10:
    print("Hoiatus: liiga palju puudumisi.")
if puudumised <= 10:
    print("Puudumiste arv on lubatud.")
    

if tööd == "ei":
    print("Kõik tööd ei ole esitatud.")
if tööd == "jah":
    print("Kõik tööd on esitatud")

if punktisumma >= 50 and puudumised <=10 and tööd == "jah":
    print("Aine on läbitud.")
else:
    print("Aine ei ole läbitud.")