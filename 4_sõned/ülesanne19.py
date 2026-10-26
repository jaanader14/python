märk = input("Sisesta tähemärk: ")
if len(märk) != 1:
    print("Viga: Palun sisesta täpselt üks tähemärk!")
else:
    if märk.lower() in "aeiouõäöü":
        print("Tegemist on täishäälikuga.")
    elif märk.lower() in "bcdfghjklmnpqrsšzžtuvwxy":
        print("Tegemsist on kaashäälikuga.")
    elif märk.isdigit():
        print("Tegemist on numbriga.")
    else:
        print("Tegemist on muu sümboliga")