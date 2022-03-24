import socket as sck
import threading as thr
import datetime as dt
import random as rnd
import time

class Recv_Manager(thr.Thread):
    def init(self,socket):
        thr.Thread.init(self) #super di Java
        self.socket=socket
        self.running=True
    def run(self):
        while self.running:
            received_msg=self.socket.recv(4096).decode()
            if(received_msg == "1"):
                print("Ricezione avvenuta")
            elif(received_msg == "2"):
                print("Ricezione avvenuta e pericolo immediato")
            elif(received_msg == "3"):
                print("Attivazione sirena luminosa")
        
listAltezze=[10, 22, 43, 12, 35]

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(('localhost',5000))
    receiver=Recv_Manager(s)
    receiver.start()

    idStazione=input("Inserire l'ID della stazione: ")


    while True:
        valAlt= listAltezze[rnd.randint(0,len(listAltezze)-1)]
        s.sendall(f"{valAlt}${idStazione}${dt.datetime.now()}".encode())
        time.spleep(15)

if __name__==__"main"__:
    main()