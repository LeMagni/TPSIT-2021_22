import threading as thr
import socket as sck
import sqlite3

threads = []
operazioni = {}

def makeOp():
    for k in range(7):
        conn = None
        conn = sqlite3.connect("operations.db")
        cur = conn.cursor()
        cur.execute(f"SELECT client, operation FROM operations")
        campi = cur.fetchall()[0]
        operazioni[campi[0]]=campi[1]
    #print(operazioni.keys())

class operazioni(thr.Thread):
     def __init__(self,connection,address,n_client):
        thr.Thread.init(self) #super di Java
        self.connection=connection
        self.address=address
        self.running=True
        self.n_client = n_client
def run(self):
        while self.running:
            for k in operazioni.keys():
                if k == n_client:
                    self.connection.sendall(operazioni[k].value().encode())
                    ris = self.connection.recv(4096).decode()
                    print (f"{operazioni[k].value()} = {ris} from {address[0]} - {address[1]}")
                    self.connection.sendall("exit".encode())

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind('localhost',5000)
    s.listen()

    cnt_client = 0

    while True:
        connection,address = s.accept()
        cnt_client = cnt_client +1
        client = operazioni(connection,address,cnt_client)

        threads.append(client)

        client.start()

        if cnt_client > 2:
            break



if __name__=="__main__":
    makeOp()
    main()
