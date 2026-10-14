cpu = int(input("CPU kasutus (%): "))
mälu = int(input("Mälu kasutus (%): "))
ketas = int(input("Ketta kasutus(%): "))
if cpu > 90 or mälu > 90 or ketas > 90:
    print("Kriitiline")
elif cpu > 75 or mälu > 75 or ketas > 75:
    print("Hoiatus")
else:
    print("OK")