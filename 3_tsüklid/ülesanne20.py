aasta = 1
raha = 1000
lisa = 1.05
while aasta <= 10:
    raha = raha * lisa
    print(f"{aasta}. aasta lõpus on konto seis {raha:.2f}")
    aasta = aasta + 1