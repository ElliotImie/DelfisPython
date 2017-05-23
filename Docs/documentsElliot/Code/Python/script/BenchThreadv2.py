# -*- coding: utf-8 -*-
from threading import Thread
import socket
import json
import time

class ThreadVelo(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):

		i = 0
		# temp1 = time.clock()
		while True :
			i += 1
		# temp2 = time.clock()
		# tempTotal = temp2 - temp1
		# print("Temps d'execution thread "  + str(tempTotal))

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
		i = 0
		tempPri = time.clock()
		while i < 10  :
			velo = ThreadVelo(i)
			velo.start()
			i += 1
		tempP2 = time.clock()
		print("Temp total : " + str(tempP2-tempPri))



lettre =""
i = 0
while True :

	try :
		lettre = input("Lancer un thread")
	except NameError, SyntaxError  :
		print("thread " + str(i))
		i += 10

	for j in range(0,10):
		ThreadVelo().start()
		print(j)
