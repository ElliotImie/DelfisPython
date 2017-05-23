# -*- coding: utf-8 -*-
from threading import Thread
import socket
import json

class ThreadVelo(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		i = 0
		print("Entrée dans le threadVelo")
		# while i<1000000 :
        #     print(i)
        #     i+=1


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
	""" Thread principal qui a pour but de renvoyer les clients sur leur Thread
		Vélo --> ThreadVelo
		Voiture --> ThreadVoiture """
	def __init__(self):
		Thread.__init__(self)

	def run(self):
    i = 0
        while i<100 :
			velo = ThreadVelo()
			velo.start()



threadPrincipal = ThreadPrincipal()
threadPrincipal.start()
threadPrincipal.join()
print("c'est finii")
