märk = input("Sisesta tähemärk:")
täishäälik = "a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"
kaashäälik =  "b", "d", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v"
number = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
if märk == täishäälik:
    print("Tegemist on täishäälikuga.")
if märk == kaashäälik:
    print("Tegemist on kaashäälikuga.")
if märk == number:
    print("Tegemist on numbriga.")
else:
    print("Tegemist on muu sümboliga")