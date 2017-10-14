import messaging 

m = messaging.messaging(input("Input your public key: "))
while True:
	t = input("Which public key's ip you want to look up?")
	print(m.iplookups(t))

