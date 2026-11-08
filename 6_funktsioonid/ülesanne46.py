def liida(a, b):
    return a + b

def lahuta(a, b):
    return a - b

def korruta(a, b):
    return a * b

def jaga(a, b):
    if b == 0:
        return "Viga: Nulliga jagamine ei ole lubatud!"
    return a / b

def kalkulaator():
    while True:
        print("\nVali tehe:")
        print("1. Liitmine (+)")
        print("2. Lahutamine (-)")
        print("3. Korrutamine (*)")
        print("4. Jagamine (/)")
        print("5. Lõpeta programm")
        
        valik = input("Sisesta valiku number (1-5): ")

        if valik == '5':
            print("Aitäh, et kasutasid kalkulaatorit. Head aega!")
            break

        if valik not in ['1', '2', '3', '4']:
            print("Vigane valik! Palun vali arv vahemikus 1-5.")
            continue

        try:
            arv1 = float(input("Sisesta esimene arv: "))
            arv2 = float(input("Sisesta teine arv: "))
        except ValueError:
            print("Viga: Palun sisesta ainult korrektseid arve!")
            continue

        if valik == '1':
            tulemus = liida(arv1, arv2)
            tehte_mark = "+"
        elif valik == '2':
            tulemus = lahuta(arv1, arv2)
            tehte_mark = "-"
        elif valik == '3':
            tulemus = korruta(arv1, arv2)
            tehte_mark = "*"
        elif valik == '4':
            tulemus = jaga(arv1, arv2)
            tehte_mark = "/"

        if isinstance(tulemus, str):
            print(tulemus)
        else:
            print(f"Tulemus: {arv1} {tehte_mark} {arv2} = {tulemus}")

kalkulaator()