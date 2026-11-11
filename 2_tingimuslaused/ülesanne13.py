punktisumma = int(input("Sisesta punktisumma: "))
if punktisumma >= 90:
    print("Hinne: 5.")
elif punktisumma >= 75:
    print("Hinne: 4.")
elif punktisumma >= 50:
    print("Hinne: 3.")
elif punktisumma >= 20:
    print("Hinne: 2.")
else:
    if punktisumma >= 0:
        print("Hinne: 1.")