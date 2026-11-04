def positiivsed(arvud):
    positiivsed_arvud = []
    for arv in arvud:
        if arv > 0:
            positiivsed_arvud.append(arv)
    return positiivsed_arvud
print(positiivsed([-4, 5, 0, 12, -2, 7]))