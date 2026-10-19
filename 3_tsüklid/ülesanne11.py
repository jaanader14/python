summa = 0
mitu_arvu = 5
for i in range (1, mitu_arvu + 1):
    arv = int(input(f"Sisesta {i}. arv: "))
    summa = summa + arv
    print(f"Arvude summa on {summa}")