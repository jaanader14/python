punktisumma = int(input("Sisesta punktisumma: "))
if punktisumma >= 90:
    print("Hinne: 5.")
else:
    if punktisumma > 75:
        print("Hinne: 4.")
    else:
        if punktisumma > 50:
            print("Hinne: 3.")
        else:
            if punktisumma > 20:
                print("Hinne: 2.")
            else:
                if punktisumma >= 0:
                    print("Hinne: 1.")