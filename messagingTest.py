import messaging
import threading
import messageProcessing
import sys
import time

def messageSender():
	while True:
<<<<<<< HEAD
		message = "~" + input("")
=======
		message = "~"+input("")
>>>>>>> ae3c47172d9c608e4f18a7cbeea0765eecbc269a
		if message!="EXIT":
			m.sendMessage(recipientPubKey, message)
		else:
			break

def messageGetter():
	while True:
		rawmsg = m.getMsgFromQ()
		if rawmsg:
			msg = messageProcessing.messageUnpacking(rawmsg, m.PrivKey)
			print()
<<<<<<< HEAD
=======
			print(msg['from']+" says:")
>>>>>>> ae3c47172d9c608e4f18a7cbeea0765eecbc269a
			print(msg['content'][1:])
			print("at "+msg['time-sent'])
			print() 
		time.sleep(1)

m = messaging.messaging()
print("My public Key is: " + m.strPubKey)
messageGetterThread = threading.Thread(target=messageGetter)
messageGetterThread.start()

while True:
	recipientPubKey = input("You wanna talk with: ")
	print(m.iplookups(recipientPubKey))
	messageSender()
