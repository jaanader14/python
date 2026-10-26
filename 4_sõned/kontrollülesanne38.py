parool = input("Sisesta parool: ")

tingimused = 0
puudused = []
if len(parool) >= 8:
    tingimused += 1
else:
    puudused.append("Parool on liiga lühike.")

if any(märk.isupper() for märk in parool):
    tingimused += 1
else:
    puudused.append("Puudub suurtäht.")

if any(märk.islower() for märk in parool):
    tingimused += 1
else:
    print("Puudub väiketäht.")

if any (märk.isdigit() for märk in parool):
    tingimused += 1
else:
    puudused.append("Puudub number.")

if any(not märk.isalnum() for märk in parool):
    tingimused += 1
else:
    puudused.append("Puudub erimärk.")

if tingimused <= 2:
    hinnang = "Nõrk parool"
elif tingimused <= 4:
    hinnang = "Keskmine parool"
else:
    hinnang = "Kõik nõuded täidetud"
print(f"Tulemus: {tingimused}/5")
print(f"Hinnang: {hinnang}")

if puudused:
    for puudus in puudused:
        print(puudus)