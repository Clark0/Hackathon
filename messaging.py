import time
from socket import *

class messaging:
	def __init__(self, myPubKey):
		self.table = {}
		self.myPubKey = myPubKey
        broadCasting = socket(AF_INET, SOCK_DGRAM)
        broadCasting.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        broadCasting.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


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

	def ask(self, targetPubKey):




	def getMyIP(self):
		s = socket(AF_INET, SOCK_DGRAM)
		s.connet(("8.8.8.8", 80))
		return s.getsockname()[0]






