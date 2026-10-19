summa = 0
mitu_arvu = int(input("Mitu arvu soovid sisestada?: "))
for i in range (1, mitu_arvu + 1):
    arv = int(input(f"Sisesta {i}. arv: "))
    summa = summa + arv
print(f"Arvude summa on {summa}")
keskmine = summa / mitu_arvu
print(f"Arvude keskmine on {keskmine}")
