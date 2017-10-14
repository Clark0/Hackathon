import time
from socket import *
import threading
from queue import Queue

class messaging:
	def __init__(self, myPubKey):
		self.broadcastQ = Queue()
		self.lock = threading.Lock()
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
		broadcasterThread = threading.Thread(target=self.broadcaster)
		broadcasterThread.start()

		self.table[self.myPubKey] = (self.myIP,float('Inf'))

	def iplookups(self, targetPubKey):
		for x in range(3):
			ip = self.iplookup(targetPubKey)
			if ip:
				return ip
			time.sleep(5)

	def iplookup(self, targetPubKey):
		try:
			targetTuple = self.table[targetPubKey]
			if time.time() - targetTuple[1] < 600:
				return targetTuple[0]
			else:
				del(self.table[targetPubKey])
				return self.iplookup(targetPubKey)

		except KeyError:
			self.ask(targetPubKey)

	def broadcaster(self):
		while True:
			task = self.broadcastQ.get()
			self.broadcast(task)
			self.broadcastQ.task_done()

	def broadcast(self, targetPubKey):
		for x in range(255):
			for y in range(255):
				try:
					self.broadCasting.sendto(targetPubKey.encode(),('10.27.'+str(x)+'.'+str(y), self.broadCastingPort))
					time.sleep(0.00005)
				except:
					time.sleep(0.0001)


	def recvAnswer(self, targetPubKey):  # received other's reply(IP addr) to my broadcasting
		while True:
			try:
				self.ipReceivingSocket.settimeout(None)
				message, Address = self.ipReceivingSocket.recvfrom(2048)
				decodedMessage = message.decode()
				if decodedMessage == targetPubKey:
					self.ipReceivingSocket.settimeout(None)
					self.table[targetPubKey] = (Address[0],time.time())
					break
			except socket.timeout:
				break

	def ask(self, targetPubKey):
		self.broadcastQ.put(targetPubKey)
		t = threading.Thread(target=self.recvAnswer,args = (targetPubKey,))
		t.start()

	def Answer(self):
		while True:
			message, Address = self.broacastReceivingSocket.recvfrom(2048)
			decodedMessage = message.decode()
			if decodedMessage != self.myPubKey:
				continue
			self.ipSendingSocket.sendto(self.myPubKey.encode(),(Address[0], self.ipReceivingPort))

	def getMyIP(self):
		s = socket(AF_INET, SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		return s.getsockname()[0]