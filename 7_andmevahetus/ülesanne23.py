import urllib.request

def kuva_esimesed_read():
    url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
    
    print(f"Teostan päringu aadressile: {url}\n")
    
    with urllib.request.urlopen(url) as vastus:
        baidid = vastus.read()
        tekst = baidid.decode("utf-8")

    read = tekst.splitlines()
    
    print("--- ESIMESED READ ---")

    for i, rida in enumerate(read[:10], start=1):
        print(f"{i}. {rida}")


kuva_esimesed_read()