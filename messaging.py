import time
from socket import *
import threading

class messaging:
	def __init__(self, myPubKey):
		self.table = {}
		self.myPubKey = myPubKey
		self.broadCastingPort = 54542
		self.ipReceivingPort = 54541
		self.myIP = self.getMyIP()
		self.broadCasting = socket(AF_INET, SOCK_DGRAM)
		self.broacastReceivingSocket = socket(AF_INET,SOCK_DGRAM)
		self.broacastReceivingSocket.bind(('',self.broadCastingPort))
		self.ipSendingSocket = socket(AF_INET,SOCK_DGRAM)
		self.ipReceivingSocket = socket(AF_INET,SOCK_DGRAM)
		self.ipReceivingSocket.bind(('',self.ipReceivingPort))

		answerThread = threading.Thread(target=self.Answer)
		answerThread.start()
		self.table[self.myPubKey] = (self.myIP,time.time())

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

	def broadcast(self, targetPubKey):
		for x in range(255):
			for y in range(255):
				try:
					self.broadCasting.sendto(targetPubKey.encode(),('10.27.'+str(x)+'.'+str(y), self.broadCastingPort))
					time.sleep(0.00005)
				except:
					time.sleep(0.0001)
		print("broadcast done!"+targetPubKey)

	def recvAnswer(self, targetPubKey):  # received other's reply(IP addr) to my broadcasting
		while True:
			try:
				self.ipReceivingSocket.settimeout(None)
				message, clientAddress = self.ipReceivingSocket.recvfrom(2048)
				decodedMessage = message.decode()
				print("Received:\n ", str(decodedMessage))
				if decodedMessage == targetPubKey:
					self.ipReceivingSocket.settimeout(None)
					self.table[targetPubKey] = clientAddress
					print("Yay")
					break
			except socket.timeout:
				break

	def ask(self, targetPubKey):
		t1 = threading.Thread(target=self.broadcast,args = (targetPubKey,))
		t2 = threading.Thread(target=self.recvAnswer,args = (targetPubKey,))
		t2.start()
		t1.start()

	def Answer(self):
		print("The server is ready to Answer")
		while True:
			message, Address = self.broacastReceivingSocket.recvfrom(2048)
			decodedMessage = message.decode()
			print("Received PubKey: "+decodedMessage+" from "+Address[0])
			if decodedMessage != self.myPubKey:
				print("continue")
				continue
			self.ipSendingSocket.sendto(self.myPubKey.encode(),(Address, self.ipReceivingPort))
			print("Answer to " + str(Address) +"\n")

	def getMyIP(self):
		s = socket(AF_INET, SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		return s.getsockname()[0]