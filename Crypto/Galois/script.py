from binascii import unhexlify
import socket

s1 = "ce1d549238dc2a"
s2 = "1ef76eeb6bae04"

print(hex(int(s1,16) ^ int(s2, 16))[2:])


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("galois.flag4all.sh", 12345))

# s.send("2")