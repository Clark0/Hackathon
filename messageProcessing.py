import re

def messagePacking(myPubKey,recipientPubKey,message):
	packedMsg = '''From: {}\r\nTo: {}\r\nMessage-Content: {}\r\n'''.format(myPubKey,recipientPubKey,message)
	return packedMsg.encode()

def messageUnpacking(packedMsg):
	message = {}
	decoded = packedMsg.decode()
	message['from'] = re.search(r"From: .*?\r\n",decoded).group().strip('From: ').strip('\r\n')
	message['to'] = re.search(r"To: .*?\r\n",decoded).group().strip('To: ').strip('\r\n')
	message['content'] = re.search(r"Message-Content: .*?\r\n",decoded).group().strip('Message-Content: ').strip('\r\n')
	return message

