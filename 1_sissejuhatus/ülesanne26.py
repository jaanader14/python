tundide_arv = int(input("Sisesta tundide arv: "))
päevade_arv = tundide_arv // 24
tundide_jääk = tundide_arv % 24
print(f"{tundide_arv} tundi on {päevade_arv} päeva ja {tundide_jääk} tundi.")