# XOR
### 460 | Débutant

XOR is perfect if the key length is the same as the message length, but that's a lot and I'm lazy, 6 characters is enough not to be broken by a brute-force attack.

Auteur : Raccoon (BZHack Friends)

#### Files:
output.txt

source.py

#### Réflexion :
Le fichier source.py nous apprend que le flag a été encoder via un XOR avec une clé random. On remarque que la clé ne fait que 6 caractère et que le message qui a été caché est composé de 12 caractères aléatoire entourés de "FLAG{}".

La clé est réutilisée de manière cyclique sur tout le text. Hors nous connaissons 6 characète du text de base : "FLAG{}". Il suffit donc de faire un XOR entre le text "FLAG{}" et sont équivalent encodé.

#### Solution :
On récupère la sous chaine présente dans Output correspondant à "FLAG{}". On réalise un XOR avec "FLAG{}" afin d'obtenir la clé puis on réalise un XOR entre la clé et l'output présent dans le fichier txt. On obtient alors le flag : 

FLAG{720b1f06572a3c7335bde6d1}
