from cryptography.hazmat.backends import default_backend #private key creation
from cryptography.hazmat.primitives.asymmetric import rsa #private key creation
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import base64

class RSAEncryptor:

	#loads a private key in pem format from a file
	def load_private_key(self, my_key_file, my_password):
		key_file = open(my_key_file, "rb")
		private_key = serialization.load_pem_private_key(
		key_file.read(),
		password=my_password,
		backend=default_backend()
		)
		return private_key
		
	#generates a private key given an exponenet and key size
	def generate_private_key(self, my_exponent, my_key_size):
		#private key creation
		private_key = rsa.generate_private_key(
			public_exponent=my_exponent,
			key_size=my_key_size,
			backend=default_backend()
			)
		return private_key
	
	#Serializes private key for storage. Provides encryption
	def serialize_private_key(self, private_key, password):	
		#Key serializaiton	
		pem = private_key.private_bytes(
			encoding=serialization.Encoding.PEM,
			format=serialization.PrivateFormat.PKCS8,
			encryption_algorithm=serialization.BestAvailableEncryption(password)
			)	
		
		return pem

	def deserialize_private_key(self, s_privatve_key, password):
		private_key = serialization.load_pem_private_key(
			s_privatve_key,
			password=password,
			backend=default_backend()
		)
		return private_key

	def serialize_public_key(self, public_key):	
		pem = public_key.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
		)
		return pem

	def deserialize_public_key(self, s_public_key):
		pem = load_pem_public_key(s_public_key, backend=default_backend())
		return pem

	#public key creation	
	def	generate_public_key(self, private_key):		
		public_key = private_key.public_key()
		return public_key
	
	#message encryption		
	def encrypt(self, public_key, my_message):	
		message = my_message #b"encrypted data"
		ciphertext = public_key.encrypt(
			message,
			padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA1()),
				algorithm=hashes.SHA1(),
				label=None
			)
		)
		return ciphertext
	
	#message decryption
	def decrypt(self, private_key, ciphertext):	
		plaintext = private_key.decrypt(
			ciphertext,
			padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA1()),
				 algorithm=hashes.SHA1(),
				label=None
			)
		)
		return plaintext	

	def decrypt_list(self, private_key, cipher_dict):
		for entry in cipher_dict:
			entry['message'] = self.decrypt(private_key,  base64.b64decode(str(entry['message'])))
		return cipher_dict
if __name__ == '__main__':
		encryptor = RSAEncryptor()
		private = encryptor.load_private_key("rsa_private.pem", None) 
		public = encryptor.generate_public_key(private)
		
		e_private = encryptor.serialize_private_key(private, b'mypassword')
		r_private = encryptor.deserialize_private_key(e_private, b'mypassword')


		#cipher_text = encryptor.encrypt(public, b"This is a test of the encryption and decryption.")
		#print "cipher text :"  + cipher_text
		
		#plaintext = encryptor.decrypt(private, cipher_text)
		
		#print "plaintext : " + plaintext