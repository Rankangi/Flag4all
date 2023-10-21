import hashlib

file = open("flag_maraboute.txt", "r")
hash = file.read().splitlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}0123456789_-"
result = [hashlib.md5(elt.encode()).hexdigest() for elt in alphabet]

txt = ""
for elt in hash:
    txt += alphabet[result.index(elt)]
print(txt)