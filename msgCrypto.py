from Crypto.PublicKey import RSA

def main():
	generateKeys()
	strPubKey, PrivKey = readKeys()
	PubKey = RSA.importKey(strPubKey.encode())

	print(type(PubKey))

	emsg = encrypt(PubKey, "shuang".encode())
	print(decrypt(PrivKey, emsg).decode())

def generateKeys():
	key = RSA.generate(1024)
	with open("PubKey.pem", "wb") as f:
		f.write(key.publickey().exportKey("PEM"))

	with open("PrivKey.pem", "wb") as f:
		f.write(key.exportKey("PEM"))

def readKeys():
	with open("PubKey.pem", "rb") as f:
		PubKey = f.read()

	with open("PrivKey.pem", "rb") as f:
		PrivKey = RSA.importKey(f.read())

	return PubKey.decode("utf-8"), PrivKey

def encrypt(PubKey, text):
	emsg = PubKey.encrypt(text, "x")[0]
	return emsg

def decrypt(PrivKey, emsg):
	text = PrivKey.decrypt(emsg)
	return text

if __name__ == "__main__":
	main()
