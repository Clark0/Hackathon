import messaging
import threading
import messageProcessing
import sys
import time

def messageSender():
	while True:
		message = "~"+input("")
		if message!="~EXIT":
			success = m.sendMessage(recipientPubKey,message)
			if not success:
				print("Connection is broken!/Unable to connect!")
				break
		else:
			break

def messageGetter():
	while True:
		rawmsg = m.getMsgFromQ()
		if rawmsg:
			msg = messageProcessing.messageUnpacking(rawmsg)
			print()
			print(msg['from']+" says:")
			print(msg['content'][1:])
			print("at "+msg['time-sent'])
			print() 
		time.sleep(1)



myPubKey = input("Input your PubKey: ")
m = messaging.messaging(myPubKey)
messageGetterThread = threading.Thread(target=messageGetter)
messageGetterThread.start()

while True:
	recipientPubKey = input("You wanna talk with: ")
	if m.sendMessage(recipientPubKey,"==Connection Test=="):
		print("Connection established")
	else:
		print("Connection failed!\nType your message to retry!")
	messageSender()
