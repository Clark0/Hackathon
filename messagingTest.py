import messaging 

m = messaging(input("Input your public key: "))
while True:
	t = input("Which public key's ip you want to look up?")
	m.iplookup(t)
