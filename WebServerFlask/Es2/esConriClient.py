import socket as sck
import threading as thr
import datetime as dt
import random as rnd
import time


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(('localhost',5000))

    while True:
        received_msg=s.socket.recv(4096).decode()
        if(received_msg == "exit"):
            s.close()
            break
        else:
            ris=eval(received_msg)
            s.sendall(ris.encode())
                
if __name__=="__main__":
    main()