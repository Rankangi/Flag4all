# Key1 = 1039380a3d3c0d0028465f0b3b016d704c1333193e7a12205a2d0812
# Key2 = 796a6d440c6a583705213558577159231276103c074e715469665a3c
# Key3 = 29011f095c24234c5654580723410665231874417a1e38121928237d
# Password^Key1^key2^Key3 = 086744430f47467f12625875283534244866180b040a4e013176744e
# Recettes confidentielles : « fichier_de_recettes.7z »

from binascii import unhexlify
import math


Key1 = "1039380a3d3c0d0028465f0b3b016d704c1333193e7a12205a2d0812"
Key2 = "796a6d440c6a583705213558577159231276103c074e715469665a3c"
Key3 = "29011f095c24234c5654580723410665231874417a1e38121928237d"
Out = "086744430f47467f12625875283534244866180b040a4e013176744e"

# P1 = hex(int(Out,16) ^ int(Key3, 16))[2:]
# P2 = hex(int(P1,16) ^ int(Key2, 16))[2:]
# P3 = hex(int(P2,16) ^ int(Key1, 16))[2:]
# k1 = hex(int(Key1,16) ^ int(Key2, 16))[2:]
# k2 = hex(int(k1,16) ^ int(Key3, 16))[2:]
# print(P3)
# print(k2)

expo = int(Key1,16) * int(Key2,16) * int(Key3,16)
print(expo)
print(int(Out,16))
print(math.log(int(Out,16)) //expo)