tooted = 0
summa = 0
print("Sisesta hind: ")
hind = float(input())
while hind != 0:
    print("Sisesta hind: ")
    hind = float(input())
    tooted += 1
    summa += hind
print(f"Tooteid: {tooted}")
print(f"Kokku: {summa}")