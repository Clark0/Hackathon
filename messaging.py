import time
from socket import *
import threading

class messaging:
	def __init__(self, myPubKey):
		self.table = {}
		self.myPubKey = myPubKey
		self.myPort = 54542

		self.broadCasting = socket(AF_INET, SOCK_DGRAM)
		self.broadCasting.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.broadCasting.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
		self.broadCasting.bind(('',self.myPort))
		
		self.mySocket = socket(AF_INET,SOCK_DGRAM)
		self.mySocket.bind(('',self.myPort + 1))
		self.mySocket.setblocking(0)

		answerThread = threading.Thread(target=self.Answer, args=(self))





	def iplookup(self, targetPubKey):
		try:
			targetTuple = self.table[targetPubKey]
			if time.time() - targetTuple[1] < 600:
				return targetTuple[0]
			else:
				del(self.table[targetPubKey])
				return self.ipLookUp(targetPubKey)

		except KeyError:
			self.ask(targetPubKey)

	def broadcast(self):
		for x in range(255):
			for y in range(255):
				try:
					self.broadCasting.sendto(targetPubKey.encode(),('10.27.'+str(x)+'.'+str(y), 54544))
					time.sleep(0.00005)
				except:
					time.sleep(0.0001)

	def recvAnswer(self):  # received other's reply(IP addr) to my broadcasting
		while True:
			try:
				self.mySocket.settimeout(10)
				message, clientAddress = self.mySocket.recvfrom(2048)
				decodedMessage = message.decode()
				print("Received:\n ", str(decodedMessage))
				if decodedMessage == targetPubKey:
					self.table[targetPubKey] = clientAddress
					break
			except socket.timeout:
				break

	def ask(self, targetPubKey):
		t1 = threading.Thread(target=self.broadcast)
		t2 = threading.Thread(target=self.recvAnswer)
		t2.start()
		t1.start()

	def Answer(self):
		answerSocket = socket(AF_INET,SOCK_DGRAM)
		answerSocket.bind(('',myPort))
		answerSocket.setblocking(0)
		print("The server is ready to Answer")
		while True:
			message, Address = answerSocket.recvfrom(2048)
			decodedMessage = message.decode()
			if decodedMessage != self.myPubKey:
				continue
			answerSocket.sendto(myPubKey.encode(),Address)
			print("Answer to " + str(Address) +"\n")

	def getMyIP(self):
		s = socket(AF_INET, SOCK_DGRAM)
		s.connet(("8.8.8.8", 80))
		return s.getsockname()[0]