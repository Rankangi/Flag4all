RSA Primes
484
Débutant

More primes, more security!
Auteur : Raccoon (BZHack Friends)

Files:
output.txt
source.py

Réflexion :
On remarque rapidement qu'il s'agit d'un RSA avec 3 nombres premiers à la place de 2. Cela ne change rien à la sécurité du RSA. Le fichier output contient n = p*q*r ainsi que p et q il suffit donc de trouver r pour pouvoir calculer d = (p-1) * (q-1) * (r-1) et pouvoir déchiffrer le text.

Solution :
L'astuce est de réaliser une division euclidienne et non une division normale pour ne pas être bloqué par les restrictions de taille de floatant de python : r = (n // p) // q
On calcul alors d et on déchiffre pour obtenir le flag :
FLAG{7c5c82d886c556bb181618ee}
