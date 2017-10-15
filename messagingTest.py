import messaging
import threading
import messageProcessing
import sys
import time
def inputPubKey():
	PubKeys = []
	print("You wanna talk with: \n")
	while True:
		try:
			PubKey = input()
		except KeyboardInterrupt:
			break
		PubKeys.append(PubKey)

	return "\n".join(PubKeys)


def messageSender():
	while True:
		message = "~" + input("")
		message = "~"+input("")
		if message != "EXIT":
			m.sendMessage(recipientPubKey, message)
		else:
			break

def messageGetter():
	while True:
		rawmsg = m.getMsgFromQ()
		if rawmsg:
			msg = messageProcessing.messageUnpacking(rawmsg, m.PrivKey)
			print()
			# print(msg['from']+" says:")
			print(msg['content'][1:])
			print("at "+msg['time-sent'])
			print() 
		time.sleep(1)

m = messaging.messaging()
print("My public Key is:")
print(m.strPubKey)
print()
messageGetterThread = threading.Thread(target=messageGetter)
messageGetterThread.start()

while True:
	with open("targetPubKey.pem", "rb") as f:
		recipientPubKey = f.read()

	print(m.iplookups(recipientPubKey))
	messageSender()



