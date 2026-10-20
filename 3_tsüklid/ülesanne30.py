from random import randint
i = 1
kull = 0
kiri = 0
while i < 101:
    vise = randint(1, 2)
    if vise == 1:
        kull = kull + 1
    else:
        kiri = kiri + 1
    i += 1
print(f"Kull: {kull}")
print(f"Kiri: {kiri}")