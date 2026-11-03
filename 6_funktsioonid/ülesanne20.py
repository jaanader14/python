def arvu_tüüp(arv):
    if arv > 0:
        return("Positiivne")
    elif arv < 0:
        return("Negatiivne")
    else:
        return("Null")

arv1 = float(input("Siseta arv: "))
tulemus = arvu_tüüp(arv1)
print(tulemus)