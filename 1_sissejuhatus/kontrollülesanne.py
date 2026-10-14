nimi = input("Sisesta oma nimi: ")
vanus = int(input("Sisesta oma vanus: "))
koolitee_pikkus = float(input("Sisesta koolitee pikkus kilomeetrites: "))
koolitee_kestus = float(input("Sisesta koolitee kestus minutites: "))
vanus2 = vanus + 1
koolitee_pikkus2 = koolitee_pikkus * 1000
tund = koolitee_kestus // 60
minut = koolitee_kestus % 60
koolitee_tundides = koolitee_kestus / 60
kiirus = koolitee_pikkus / koolitee_tundides
print(f"Tere, {nimi}!")
print(f"Järgmisel aastal oled {vanus2}-aastane.")
print(f"Sinu koolitee pikkus on {koolitee_pikkus2} meetrit.")
print(f"Koolitee kestab {tund} tundi ja  {minut} minutit.")
print(f"Keskmine kiirus on {kiirus} km/h.")