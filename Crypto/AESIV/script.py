from Crypto.Cipher import AES
from os import urandom
from binascii import hexlify, unhexlify

plaintext = "15fd32c552b0965c13830645fae64b12c90873b780e4dfa4afe4f122d0178bf4"
plaintext = unhexlify(plaintext)
s1 = plaintext[16:].hex()
s2 = plaintext[:16].hex()
print(hex(int(s1,16) ^ int(s2, 16))[2:])