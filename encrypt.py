from Crpto.PublicKey import RSA
from messaging import messaging

def main():
	key = RSA.generate(2048)

	with open("PriKey.pem", "w") as f:
		f.write(key.exportKey())

	with open("PubKey.pem", "w") as f:
		f.write(key.publickey().exportKey())

	with open("PubKey.pem", "r") as f:
		Pubkey = f.read()

	with open("PriKey.pem", "r") as f:
		PriKey = f.read()

	print(PubKey)
	print(PriKey)

	client = messaging(PubKey)

if __name__ == "__main__":
	main()
