
class CaesarCipher(object):
	def __init__(self, key):
		self.key = key
		self.character = list(chr(i) for i in range(123))
		self.char_len = len(self.character)

	def __crypter(self, mode, message):
		output_text = ""
		for symbol in message:
			if symbol in self.character:
				symbol_location = self.character.index(symbol)
			else:
				return "Invalid Character"

			if mode == 'encrypt':
				cipher_location = symbol_location + self.key
			elif mode == 'decrypt':
				cipher_location = symbol_location - self.key

			if cipher_location >= self.char_len:
				cipher_location = cipher_location - self.char_len
			elif cipher_location < 0:
				cipher_location = cipher_location + self.char_len

			output_text = output_text + self.character[cipher_location]
		return output_text

	def encrypt(self, message):
		encrypted_text = self.__crypter('encrypt', message)
		return encrypted_text

	def decrypt(self, message):
		decrypted_text = self.__crypter('decrypt', message)
		return decrypted_text


	
cipher = CaesarCipher(10)
message = "Hello there"
enc = cipher.encrypt(message)
print(enc)
dec = cipher.decrypt("Rovvy*roo")
print(dec)