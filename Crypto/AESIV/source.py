from Crypto.Cipher import AES
from os import urandom
from binascii import hexlify, unhexlify

key = urandom(16)
iv = urandom(16)
flag = "FLAG{" + iv.hex() + "}"
aes = AES.new(key, AES.MODE_CBC, iv)
ciphertext = bytes(32)
plaintext = aes.decrypt(ciphertext)
print(iv)
s1 = plaintext.hex()[:32]
iv = 16 * '\x00'
aes = AES.new(key, AES.MODE_CBC, iv)
plaintext = aes.decrypt(ciphertext)
s2 = plaintext.hex()[:32]
print(s2)
print(unhexlify(hex(int(s1,16) ^ int(s2, 16))[2:]))