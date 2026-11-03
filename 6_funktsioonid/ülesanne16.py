def teisenda_sekundid(sekundid):
    tunnid = sekundid // 3600

    ülejääk = sekundid % 3600

    minutid = ülejääk // 60

    ülejääk2 = ülejääk % 60

    return tunnid, minutid, ülejääk2

test = 3675
t, m, s = teisenda_sekundid(test)

print(f"Algne sekundite arv: {test}")
print(f"Tagastatud väärtused: {t}, {m}, {s}")
print(f"Ehk kokku: {t} tund, {m} minut ja {s} sekundit.")