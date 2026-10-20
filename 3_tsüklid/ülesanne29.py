from random import randint
i = 1
tulemus = 0
while i < 101:
    vise = randint(1, 6)
    if vise == 6:
        tulemus = tulemus + 1
    i += 1
print("Täringut visati 100 korda")
print(f"Kuus saadi {tulemus} korda")