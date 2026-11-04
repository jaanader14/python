def sõnade_pikkused(sõnad):
    sõnade_arv = []
    for sõna in sõnad:
        sõna1 = len(sõna)
        sõnade_arv.append(sõna1)
    return sõnade_arv
print(sõnade_pikkused(["Python", "Java", "C"]))