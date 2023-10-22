Crypt My Loop
25
Débutant

Un flag a été marabouté ! Retrouvez le.
Some magic on the flag ! Fint it.
Auteur : K_lfa (BZHack / ESDAcademy)

Files: 
flag_maraboute.txt

Réflexion :
Le fichier flag_maraboute.txt semble contenir une liste de hash. Une raide recherche via https://www.tunnelsup.com/hash-analyzer/ nous montre qu'il s'agit de md5.
Je remarque aussi que certains hash sont présent plusieurs fois. Il doit donc s'agir du hash d'un unique caractère.

Solution :
On bruteforce l'ensemble des caractères classique (lettre, chiffre caractère spéciaux)
On lance le script et un hash n'arrive pas à être découvert alors on utilise un site tel que https://10015.io/tools/md5-encrypt-decrypt pour trouver le caractère qui correspond au flah et on l'ajoute à l'alphabet.
On recommance jusqu'à obtenir l'ensemble du flag :
iletaitunefoisunflagFLAG{md5_really_sucks}
