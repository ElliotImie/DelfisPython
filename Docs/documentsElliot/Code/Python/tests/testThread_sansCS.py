from threading import Thread
import socket
import json

class ThreadVelo(Thread):
	def __init__(self):
		Thread.__init__(self)
	
	
	def run(self):
		""" Réceptionne le json envoyé par le client et insert ces coordonnées dans la base de donnée	"""
		
		i = 0
		print("Entré dans le Thread vélo")
		
		while i< 5 :			
			#msg = conn.recv(1024)
			#print("Connection établie")
			#print(type(msg))
			msg = open("exempleJson.json").read()
			message = json.loads(msg)
			print(type(message))
			print(message)
			i+=1 
			
			
		
class ThreadVoiture(Thread):
	def __init__():
		Thread.__init__(self)
		#self.conn = conn
		#self.addr = addr
		
	
	def run(self):
		""" Réceptionne le json envoyé par le client et recherche le nombre de
		 vélo dans la base de donnée	
		"""
		
		i = 0
		
		while i< 5 :			
			#msg = conn.recv(1024)
			#print("Connection établie")
			#print(type(msg))
			msg = open("exempleJson.json").read()
			message = json.loads(msg)
			print(type(message))
			print(message)
			i+=1 
			
		

	
	
	
	
	
class ThreadPrincipal(Thread):
	""" Thread principal qui a pour but de renvoyer les clients sur leur	
	Thread """

	def __init__(self):
		Thread.__init__(self)
	
	def run(self):
		
		#soc = socket.socket()
		#host = ""
		#port = 3307
		#soc.bind((host,port))
		#soc.listen(5)
		
		i = 1 
		
		while i < 2 : 
		#	conn,addr = soc.accept()
		#	print("connection etablie")
			
		#	msg = conn.recv(1024)
		#	print(type(msg))
		#	print(msg)
		#	message = json.loads(msg.decode())
		#	print(message)
		
			msg = open("exempleJson.json").read()
			print(type(msg))
			print(msg)
			message = json.loads(msg)
			
			print(type(message))
			print(message["id_user"])		
			
			if message["id_user"] == 1 :
				ThreadVelo().start()
			
			elif message["id_user"] == 2 : 
				ThreadVoiture().start()
			
			else :
				print("La récupération du type de véhicule a échoué")
			
			i+=1 
				
threadPrincipal = ThreadPrincipal()
threadPrincipal.start()
