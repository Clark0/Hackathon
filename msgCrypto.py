from Crypto.PublicKey import RSA
from base64 import b64decode
from messaging import messaging

def main():
	generateKeys()
	PubKey, PrivKey = readKeys()
	emsg = encrypt(PubKey, "shuang")
	print(decrypt(PrivKey, emsg))

def generateKeys():
	key = RSA.generate(1024)
	with open("PubKey.pem", "wb") as f:
		f.write(key.publickey().exportKey("PEM"))

	with open("PrivKey.pem", "wb") as f:
		f.write(key.exportKey("PEM"))

def readKeys():
	with open("PubKey.pem", "rb") as f:
		PubKey = RSA.importKey(f.read())

	with open("PrivKey.pem", "rb") as f:
		PrivKey = RSA.importKey(f.read())

	return PubKey, PrivKey

def encrypt(PubKey, text):
	emsg = PubKey.encrypt(text.encode(), "x")[0]
	return emsg

def decrypt(PrivKey, emsg):
	text = PrivKey.decrypt(emsg)
	return text.decode()

if __name__ == "__main__":
	main()
'''def _decrypt_rsa(decrypt_key_file, cipher_text):
    from Crypto.PublicKey import RSA
    from base64 import b64decode

    key = open(decrypt_key_file, "r").read()
    rsakey = RSA.importKey(key)
    raw_cipher_data = b64decode(cipher_text)
    decrypted = rsakey.decrypt(raw_cipher_data)
    return decrypted'''