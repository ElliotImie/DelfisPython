# -*- coding: utf-8 -*-
from threading import Thread
import socket
import json
import mysql.connector

class ThreadPrincipal(Thread):
    """ Thread principal qui a pour but de renvoyer les clients sur leur Thread """
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ""
        port = 3507
        soc.bind((host,port))
        soc.listen(5)

        conn,addr = soc.accept()
        print("connection etablie")

        connBDD = mysql.connector.connect(host="localhost", user="root", password="root", database="delfis")
        cursor = connBDD.cursor()
        while True  :

            msg = conn.recv(1024)
            message = json.loads(msg[2:]) # Converti le JSON envoyé en dictionnaire Python ( le [2:]
											# 			permet de supprimer les caractères parasites..)

            if(message["id_user"] == 0):
                break

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usr_30(
                id varchar(20) NOT NULL,
                latitude decimal(10,8) NOT NULL,
                longitude decimal(10,8) NOT NULL
            );
            """)

            cursor.execute("INSERT INTO usr_30 (id,latitude,longitude) VALUES (\" " + message["id_user"] + " \" , \" "+ message["latitude"] + " \" , \" "+ message["longitude"] +" \" );")
            connBDD.commit()
            print("insert OK")

        connBDD.close

threadPrincipal = ThreadPrincipal()
threadPrincipal.start()
threadPrincipal.join()
print("c'est finii")
