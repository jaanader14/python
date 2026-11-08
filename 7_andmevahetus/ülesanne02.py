with open("tervitus.txt", "r", encoding="utf-8") as fail:
    for järjekorranumber, rida in enumerate(fail, start=1):
        puhas_rida = rida.strip()

        print(f"{järjekorranumber}: {puhas_rida}")