import urllib.request

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

try:
    with urllib.request.urlopen(url) as response:
        sisu = response.read().decode('utf-8')

    read = sisu.splitlines()

    ridade_arv = len(read)
    tuhjade_ridade_arv = sum(1 for rida in read if not rida.strip())
    sonade_arv = len(sisu.split())
    tahemarkide_arv = len(sisu)

    print("Veebiteksti statistika")
    print(f"Ridu: {ridade_arv}")
    print(f"Sõnu: {sonade_arv}")
    print(f"Tähemärke: {tahemarkide_arv}")
    print(f"Tühje ridu: {tuhjade_ridade_arv}")

except Exception as e:
    print(f"Viga faili lugemisel: {e}")