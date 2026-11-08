def keskmine(punktid):
    if not punktid:
        return 0
    return sum(punktid) / len(punktid)

def parim_tulemus(punktid):
    if not punktid:
        return None

    parim = punktid[0]
    for punkt in punktid:
        if punkt > parim:
            parim = punkt
    return parim

def nõrgim_tulemus(punktid):
    if not punktid:
        return None

    nõrgim = punktid[0]
    for punkt in punktid:
        if punkt < nõrgim:
            nõrgim = punkt
    return nõrgim

def edukate_arv(punktid, piir=50):
    loendur = 0
    for punkt in punktid:
        if punkt >= piir:
            loendur += 1
    return loendur

kontrolltöö_punktid = [78, 45, 92, 67, 34, 100, 56, 81]

kesk = keskmine(kontrolltöö_punktid)
parim = parim_tulemus(kontrolltöö_punktid)
nõrgim = nõrgim_tulemus(kontrolltöö_punktid)
edukad_50 = edukate_arv(kontrolltöö_punktid)
edukad_70 = edukate_arv(kontrolltöö_punktid, piir=70)

print(f"Õpilaste punktid: {kontrolltöö_punktid}")
print(f"Klassi keskmine tulemus:  {kesk:.1f} punkti")
print(f"Parim saavutatud tulemus: {parim} punkti")
print(f"Nõrgim saavutatud tulemus: {nõrgim} punkti")
print(f"Edukate arv (vähemalt 50p): {edukad_50} õpilast")
print(f"Edukate arv (vähemalt 70p): {edukad_70} õpilast")