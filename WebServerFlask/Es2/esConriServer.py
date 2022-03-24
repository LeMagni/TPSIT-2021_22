import socket as sck
import threading as thr
import logging
import sqlite3

clientsTHR={}
operazioni={}


def caricaOp():
    for k in
    conn = sqlite3.connect("operations.db") #crea una "connessione" col database
    cur = conn.cursor()
    cur.execute(f"SELECT client, operation FROM operations") #esegue la query indicata per trovare la sequenza giusta tramite il nome
    dati = cur.fetchall()[0]

class Client_Manager(thr.Thread):
    def __init__(self,connection,address,nClient):
        thr.Thread.__init__(self) #super di Java
        self.connection=connection
        self.address=address
        self.running=True
        self.nClient=nClient

    def run(self):
        while self.running:
            msg=self.connection.recv(4096).decode() #aspetta di ricevere un messaggio (nome del comando) dal client
            msg=msg.split("$")
            conn = sqlite3.connect("fiumi.db") #crea una "connessione" col database
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM fiumi WHERE id_stazione = '{int(msg[1])}'") #esegue la query indicata per trovare la sequenza giusta tramite il nome
            dati = cur.fetchall()[0][0]
            lv30=dati[3]*30/100
            lv70=dati[3]*70/100

            print(f"{msg[2]}:{dati[2].upper()},{dati[1]}\n")

            if(msg[0]<lv30):
                self.connection.sendall("1".encode())
                print("Ricezione avvenuta")
            elif(msg[0]>=lv30 and msg[0]<lv70):
                self.connection.sendall("2".encode())
                print("Ricezione avvenuta e pericolo immediato")
            elif(msg[0]>=lv70):
                self.connection.sendall("3".encode())
                print("Attivazione sirena luminosa")

            cur.close()

            print (f"{operazione} = {risultato} from {client_ip} - {client_port}")

def main():
    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.bind(("localhost",5000))
    s.listen()
    clnt=0

    while True:
        connection, address=s.accept()
        clnt=clnt+1
        client=Client_Manager(connection, address, clnt)
        clientsTHR.appends(client)
        client.start()

        if clnt>2:
            break

if __name__=="__main__":
    main()