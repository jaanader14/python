import urllib.request

def teosta_veebiparing():
    url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
    
    print(f"Teostan päringu aadressile: {url}\n")
    
    with urllib.request.urlopen(url) as vastus:
        baidid = vastus.read()
        
        tekst = baidid.decode("utf-8")

        print("--- VEEBIST LOETUD TEKST ---")
        print(tekst)

teosta_veebiparing()