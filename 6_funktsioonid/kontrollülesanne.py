def lisa_õpilane(nimed, punktid, nimi, tulemus):
    if nimi.lower() in [n.lower() for n in nimed]:
        print(f"Viga: Õpilane nimega '{nimi}' on juba süsteemis!")
        return False
    
    nimed.append(nimi)
    punktid.append(tulemus)
    print(f"Õpilane {nimi} ({tulemus} p) edukalt lisatud.")
    return True

def arvuta_hinne(punkt):
    if punkt >= 90:
        return 5
    elif punkt >= 75:
        return 4
    elif punkt >= 50:
        return 3
    elif punkt >= 20:
        return 2
    else:
        return 1

def leia_keskmine(punktid):
    if not punktid:
        return 0.0
    return sum(punktid) / len(punktid)

def leia_parim(nimed, punktid):
    if not punktid:
        return None, 0
    
    suurim_punkt = punktid[0]
    parim_indeks = 0
    
    for i in range(1, len(punktid)):
        if punktid[i] > suurim_punkt:
            suurim_punkt = punktid[i]
            parim_indeks = i
            
    return nimed[parim_indeks], suurim_punkt

def leia_nõrgim(nimed, punktid):
    if not punktid:
        return None, 0
    
    väikseim_punkt = punktid[0]
    nõrgim_indeks = 0
    
    for i in range(1, len(punktid)):
        if punktid[i] < väikseim_punkt:
            väikseim_punkt = punktid[i]
            nõrgim_indeks = i
            
    return nimed[nõrgim_indeks], väikseim_punkt

def kuva_opilased(nimed, punktid):
    if not nimed:
        print("\nSüsteemis pole veel ühtegi õpilast.")
        return

    print(f"\n{'Nimi':<15} | {'Punktid':<7} | {'Hinne':<5}")
    for i in range(len(nimed)):
        hinne = arvuta_hinne(punktid[i])
        print(f"{nimed[i]:<15} | {punktid[i]:<7} | {hinne:<5}")

def kuva_statistika(nimed, punktid):
    koguarv = len(nimed)
    print(f"Õpilasi kokku: {koguarv}")
    
    if koguarv == 0:
        print("Keskmine punktisumma: 0.00")
        print("Andmed puuduvad.")
        return

    keskmine = leia_keskmine(punktid)
    parim_nimi, parim_p = leia_parim(nimed, punktid)
    nõrgim_nimi, nõrgim_p = leia_nõrgim(nimed, punktid)
    
    print(f"Keskmine punktisumma: {keskmine:.2f}")
    print(f"Parim tulemus: {parim_nimi} ({parim_p} p)")
    print(f"Nõrgim tulemus: {nõrgim_nimi} ({nõrgim_p} p)")

    jaotus = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    for p in punktid:
        h = arvuta_hinne(p)
        jaotus[h] += 1
        
    print("\nHinnete jaotus:")
    for hinne in sorted(jaotus.keys(), reverse=True):
        print(f"Hinne {hinne}: {jaotus[hinne]} õpilane{'t' if jaotus[hinne] != 1 else ''}")

def otsi_õpilane(nimed, punktid, nimi):
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            return i
    return None

def kuva_menuu(erinev_pealkiri="ÕPILASTE HINNETE SÜSTEEM"):
    print(f"{erinev_pealkiri:^33}")
    print("1. Lisa õpilane")
    print("2. Kuva klassi õpilased")
    print("3. Kuva klassi statistika")
    print("4. Otsi õpilast nime järgi")
    print("0. Välju")

def main():
    nimed = ["Mari", "Jaan", "Kati"]
    punktid = [87, 64, 95]
    
    while True:
        kuva_menuu()
        valik = input("Vali tegevus: ").strip()
        
        if valik == '1':
            nimi = input("Sisesta õpilase nimi: ").strip()
            if not nimi:
                print("Viga: Nimi ei tohi olla tühi!")
                continue
            
            try:
                tulemus = int(input("Sisesta punktisumma (0-100): "))
                if tulemus < 0 or tulemus > 100:
                    print("Viga: Punktisumma peab olema vahemikus 0–100!")
                    continue
            except ValueError:
                print("Viga: Punktisumma peab olema täisarv!")
                continue
                
            lisa_õpilane(nimed, punktid, nimi, tulemus)
            
        elif valik == '2':
            kuva_opilased(nimed, punktid)
            
        elif valik == '3':
            kuva_statistika(nimed, punktid)
            
        elif valik == '4':
            otsitav = input("Sisesta otsitava õpilase nimi: ").strip()
            indeks = otsi_õpilane(nimed, punktid, otsitav)
            
            if indeks is not None:
                p = punktid[indeks]
                h = arvuta_hinne(p)
                print(f"\nLeitud: {nimed[indeks]} | Punktid: {p} p | Hinne: {h}")
            else:
                print(f"\nÕpilast nimega '{otsitav}' ei leitud.")
                
        elif valik == '0':
            print("\nProgrammi töö on lõpetatud. Head päeva!")
            break
            
        else:
            print("\nVigane menüüvalik! Palun vali number 0-4.")

if __name__ == "__main__":
    main()