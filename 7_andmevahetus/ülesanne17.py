def lisa_ostunimekirja():
    tooted = []
    
    while True:
        toode = input("Sisesta toode: ")
        
        if toode.upper() == "STOP":
            break
            
        tooted.append(toode)

    with open("ostunimekiri.txt", "a", encoding="utf-8") as fail:
        for toode in tooted:
            fail.write(toode + "\n")
            
    print("Ostunimekiri salvestatud.")

lisa_ostunimekirja()