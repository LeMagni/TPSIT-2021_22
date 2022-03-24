import json
import requests
import string
from urllib import request

def main():
    print("chucknorris.io:\n")
    print("Vuoi una frase di chucknorris:\n 1. In cui è presente una parola a tua scelta\n 2. Per categoria")
    opz=input("scegli la tipologia di ricerca: ")
    if(opz=='1'):
        word=input("\nscegli la parola da cercare: ")
        #print(f"https://api.chucknorris.io/jokes/search?query={word}")
        r = requests.get(f"https://api.chucknorris.io/jokes/search?query={word}")
        for k in json.loads(r.text)['result']:
            print(k['value'])
    else:
        r = requests.get("https://api.chucknorris.io/jokes/categories")
        print(r.json())
        cat=input("\nScegli una categoria tra quelle proposte sopra: ")
        r = requests.get(f"https://api.chucknorris.io/jokes/random?category={cat}")
        file = r.json()
        frase = file['value']
        print(frase)
if __name__=="__main__":
    main()