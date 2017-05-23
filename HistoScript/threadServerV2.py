# -*- coding: utf-8 -*-
from threading import Thread
import socket
import json
import mysql.connector

class ThreadVelo(Thread):

	def __init__(self,conn, addr):
		Thread.__init__(self)
		self.connexion = conn
		self.addr = addr
		self.connBDD = mysql.connector.connect(host="localhost", user="root", password="root", database="delfis")
		self.cursor = self.connBDD.cursor()


	def run(self):
		""" Réceptionne le json envoyé par le client et insert ces coordonnées dans la base de donnée """
		i = 0
		print("Entrée dans le threadVelo")
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS usr_45(
			id varchar(20) NOT NULL,
			latitude varchar(10) NOT NULL,
			longitude varchar(10) NOT NULL
		);
		""")

		while True :
			msg = self.connexion.recv(1024)
			print(type(msg))
			print(msg)

			message = json.loads(msg[2:])
			print(message)
			print(message["id_user"])
			if(message["id_user"] == "0"):
				break

			self.cursor.execute("INSERT INTO usr_49 (id,latitude,longitude) VALUES (\" " + message["id_user"] + " \" , \" "+ message["latitude"] + " \" , \" "+ message["longitude"] +" \" );")
			self.connBDD.commit()
			print("insert OK")
			self.connBDD.close


class ThreadVoiture(Thread):
	def __init__(self,conn, addr):
		Thread.__init__(self)
		self.connexion = conn
		self.addr = addr

	def run(self):
		""" Réceptionne le json envoyé par le client et recherche le nombre de vélo dans la base de donnée """
		i = 0

		while i < 5 :
			print("Entré dans le threadVoiture")
			# msg = connexion.recv(1024)
			# message = json.loads(msg)
			# print(message)
			i += 1
			print(i)


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

		while True  :
			conn,addr = soc.accept()
			print("connection etablie")
			msg = conn.recv(1024)

			message = json.loads(msg[2:]) # Converti le JSON envoyé en dictionnaire Python ( le [2:]
											# 			permet de supprimer les caractères parasites..)
			print("id_user : " + message["id_user"])
			print("latitude : " + message["latitude"])

			if message["id_user"] == "1" :
				print(conn)
				velo = ThreadVelo(conn, addr)
				velo.start()
				velo.join()
				print('fin du ThreadVelo')
				break

threadPrincipal = ThreadPrincipal()
threadPrincipal.start()
threadPrincipal.join()
print("c'est finii")
