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
<<<<<<< HEAD
<<<<<<< HEAD
		message = "~" + input("")
		message = "~"+input("")
		if message != "EXIT":
			m.sendMessage(recipientPubKey, message)
=======
=======
>>>>>>> parent of ae3c471... Fixed lost prefix in msg-content
		message = input("")
		if message!="EXIT":
			m.sendMessage(recipientPubKey,message)
>>>>>>> parent of ae3c471... Fixed lost prefix in msg-content
		else:
			break

def messageGetter():
	while True:
		rawmsg = m.getMsgFromQ()
		if rawmsg:
			msg = messageProcessing.messageUnpacking(rawmsg, m.PrivKey)
			print()
<<<<<<< HEAD
<<<<<<< HEAD
			# print(msg['from']+" says:")
			print(msg['content'][1:])
=======
			print(msg['from']+" says:")
			print(msg['content'])
>>>>>>> parent of ae3c471... Fixed lost prefix in msg-content
=======
			print(msg['from']+" says:")
			print(msg['content'])
>>>>>>> parent of ae3c471... Fixed lost prefix in msg-content
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



