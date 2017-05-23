# -*- coding: utf-8 -*-

from threading import Thread
import socket
import json

class ThreadVelo(Thread):

	def __init__(self,conn, addr):
		Thread.__init__(self)
		self.connexion = conn
		self.addr = addr

	def run(self):
		""" Réceptionne le json envoyé par le client et insert ces coordonnées dans la base de donnée """
		i = 0
		print("Entrée dans le threadVelo")

		while i < 4 :
			msg = self.connexion.recv(1024)
			print(type(msg))
			print(msg)
		
			message = json.loads(msg[2:])
			print(message)
			print(message["latitude"])
			i += 1

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

			print(msg)
			#POUR VERIFIER :
			#print(msg)
			#print(type(msg))
			#message = msg[2:]

			message = json.loads(msg[2:]) # Converti le JSON envoyé en dictionnaire Python ( le [2:]
											# 			permet de supprimer les caractères parasites..)
			print("id_user : " + message["id_user"])
			print("latitude : " + message["latitude"])
			#
			# if message["type"] == "velo" :
			# 	ThreadVelo(conn,addr).start()
			#
			# elif message["type"] == "voiture" :
			# 	ThreadVoiture(conn,addr).start()
			#
			# else :
			# 	print("La récupération du type de véhicule a échoué")
			#
			if message["id_user"] == "1" :
				print(conn)
				velo = ThreadVelo(conn, addr)
				velo.start()
				velo.join()
				print('fin du ThreadVelo')
				break



		#i+=0

threadPrincipal = ThreadPrincipal()
threadPrincipal.start()
threadPrincipal.join()
print("c'est finii")
