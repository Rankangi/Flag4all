AES IV
486
Débutant

I lost my IV, can you help me to recover it?
Auteur : Raccoon (BZHack Friends)

Files:
output.txt
source.py

Réflexion :
On remarque que la fonction utilisée n'est pas celle de chiffrement mais de déchiffrement. On remarque aussi que le ciphertext qui est utilisé correspond à un bloc de byte nulle. Le text utilisé a une taille de 32 et la clé une taille de 16 il y aura donc un découpage en 2 du text. Avec P_i = D_k(C_i) XOR C_(i-1) et C_0 = IV
On obtient alors P_2 = D_k(C_2) XOR C_1 = D_k(C_2) = D_k(C_1)
et P_1 = D_k(C_1) XOR C_0 = D_k(C_1) XOR IV
On retrouve donc IV = P_1 XOR D_k(C_1) = P_1 XOR P_2

Solution :
On découpe l'output en 2 puis on réalise un XOR entre les deux afin d'obtenir le vecteur initial : dcf54172d25449f8bc67f7672af1c0e6
On obtient alors le flag : FLAG{dcf54172d25449f8bc67f7672af1c0e6}
