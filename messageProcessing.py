import re
import time
import datetime
import msgCrypto
from Crypto.PublicKey import RSA
def messagePacking(recipientPubKey,message):
	# packedMsg = '''From: {}\r\nTo: {}\r\nMessage-Content: {}\r\nTime-Sent: {}\r\n'''.format(myPubKey,recipientPubKey,message,time.time())
	packedMsg = '''Message-Content: {}\r\nTime-Sent: {}\r\n'''.format(message, time.time())

	pubKey = RSA.importKey(recipientPubKey)
	emsg = msgCrypto.encrypt(pubKey, packedMsg)
	return emsg

def messageUnpacking(packedMsg, PrivKey):
	message = {}
	decoded = msgCrypto.decrypt(PrivKey, packedMsg)
	# message['from'] = re.search(r"From: .*?\r\n",decoded).group().strip('From: ').strip('\r\n')
	# message['to'] = re.search(r"To: .*?\r\n",decoded).group().strip('To: ').strip('\r\n')
	message['content'] = re.search(r"Message-Content: .*?\r\n",decoded).group().strip('Message-Content: ').strip('\r\n')
	message['time-sent'] = datetime.datetime.fromtimestamp(round(float(re.search(r"Time-Sent: .*?\r\n",decoded).group().strip('Time-Sent: ').strip('\r\n')))).utcnow().strftime("%a, %d %b %Y %X %z")

	return message

