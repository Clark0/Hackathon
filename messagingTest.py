import messaging
import threading
import messageProcessing
import sys

def messageSender():
	while True:
		message = input("")
		if message!="EXIT":
			m.sendMessage(recipientPubKey,message)
		else:
			break

def messageGetter():
	while True:
		rawmsg = m.getMsgFromQ()
		if rawmsg:
			msg = messageProcessing.messageUnpacking(rawmsg)
			print()
			print(msg['from']+" says:")
			print(msg['content'])
			print("at "+msg['time-sent'])
			print() 



myPubKey = input("Input your PubKey: ")
m = messaging.messaging(myPubKey)
messageGetterThread = threading.Thread(target=messageGetter)
messageGetterThread.start()

while True:
	recipientPubKey = input("You wanna talk with: ")
	messageSender()
