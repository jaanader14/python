tooted = []
hinnad = []

while True:
    toode = input("Sisesta toote nimi (lõpetamiseks ENTER): ").strip()

    if toode == "":
        break

    while True:
        try:
            hind = float(input(f"Sisesta toote '{toode}' hind: "))
            if hind >= 0:
                break
            else:
                print("Hind ei saa olla negatiivne! Proovi uuesti.")
        except ValueError:
            print("Palun sisesta korrektne number!")

    tooted.append(toode)
    hinnad.append(hind)
    print()

if len(tooted) > 0:
    print("OSTUKORVI SISU:")

    for i in range(len(tooted)):
        print(f"- {tooted[i]}: {hinnad[i]:.2f} €")

    toodete_arv = len(tooted)
    kogumaksumus = sum(hinnad)

    kalleim_hind = max(hinnad)
    kalleima_indeks = hinnad.index(kalleim_hind)
    kalleim_toode = tooted[kalleima_indeks]
    
    print(f"Toodete arv: {toodete_arv}")
    print(f"Kogumaksumus: {kogumaksumus:.2f} €")
    print(f"Kõige kallim toode: {kalleim_toode} ({kalleim_hind:.2f} €)")

    try:
        soodus_protsent = float(input("Sisesta allahindluse protsent: "))

        allahindlus = kogumaksumus * (soodus_protsent / 100)
        uus_kogumaksumus = kogumaksumus - allahindlus
        
        print(f"Soodustus ({soodus_protsent}%): -{allahindlus:.2f} €")
        print(f"Uus kogumaksumus: {uus_kogumaksumus:.2f} €")
    except ValueError:
        print("Vigane protsendi sisestus. Allahindlust ei rakendatud.")

else:
    print("\nOstukorv on tühi!")