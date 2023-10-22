import binascii

def xor(msg, key):
	return bytes([char^key[i%len(key)] for i, char in enumerate(msg)])

plaintext = "FLAG{}"
ciphertext = "889a67aab9bbfce644dca4bcf8e311dfa3bfade115def7eeaab31089f3f1"
c_flag = ciphertext[:10]+ciphertext[-2:]

new_key = xor(plaintext.encode(), binascii.unhexlify(c_flag))
print(xor(binascii.unhexlify(ciphertext), new_key).decode())