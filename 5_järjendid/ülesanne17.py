algus = int(input("Sisesta alguse arv: "))
lõpp = int(input("Sisesta lõpp arv: "))
summa = 0
while algus <= lõpp:
    summa += algus
    algus += 1
print(f"Summa: {summa}")