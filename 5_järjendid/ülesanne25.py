arvud = [4, 7, 4, 9, 2, 7, 5, 9, 1, 2]
unikaalsed_arvud = []

for arv in arvud:
    if arv not in unikaalsed_arvud:
        unikaalsed_arvud.append(arv)
print(unikaalsed_arvud)