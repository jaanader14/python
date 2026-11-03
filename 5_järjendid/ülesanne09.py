ostukorv = []

print("Palun sisesta viis toodet: ")
for i in range(5):
    toode = input(f"Sisesta {i+1}. toode:")
    ostukorv.append(toode)
    i += 1
print(ostukorv)
print(f"Ostukorvis on kokku {len(ostukorv)} toodet.")
