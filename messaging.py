import time
from socket import *
from collections import deque

class messaging:
	def __init__(self, myPubKey):
		self.table = {}
		self.myPubKey = myPubKey
		self.messageQueue = deque()
		self.broadCasting = socket(AF_INET, SOCK_DGRAM)
		self.broadCasting.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.broadCasting.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
		self.myPort = 54542


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

	# def ask(self, targetPubKey):


	def getMyIP(self):
		s = socket(AF_INET, SOCK_DGRAM)
		s.connet(("8.8.8.8", 80))
		return s.getsockname()[0]

	def dequeMessage(self):
		item = messageQueue.get(block=True, timeout=None)
		if item is not None:
			return item

	def sendMessage(self, IP, message):
		myIP = self.getMyIP()
		s = socket(AF_INET, socket.SOCK_STREAM)
		s.connet(IP, self.myPort)
		s.send(IP, message.decode)
		s.close()









