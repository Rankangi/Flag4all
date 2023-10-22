from Crypto.Cipher import AES
from os import urandom

key = urandom(16)
iv = urandom(16)
print(iv)
flag = "FLAG{" + iv.hex() + "}"
aes = AES.new(key, AES.MODE_CBC, iv)
ciphertext = bytes(32)
print(ciphertext)
plaintext = aes.decrypt(ciphertext)
print(plaintext)
