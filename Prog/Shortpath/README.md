Shortpath
484
Intermediaire

L'objectif est de trouver la longueur du chemin pour aller de l'entrée du labyrinthe (en haut à gauche) à la sortie (en bas à droite) ! Attention car malgré l'affichage qui est trompeur le labyrinthe à un format carré shortpath.flag4all.sh port 2000
Auteur : MAYO (ESDAcademy - ENI Rennes - RESD05)

Output :
[]  [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
[]              []              []      []          []              []
[][][][][][][]  []  [][][][][]  []  []  []  [][][]  [][][]  [][][]  []
[]          []  []      []          []  []      []          []      []
[]  [][][][][]  []  []  [][][][][][][]  []  []  [][][][][][][]  [][][]
[]              []  []              []  []  []  []          []      []
[]  [][][][][][][][][][][]  [][][]  []  [][][]  []  [][][]  [][][]  []
[]          []          []      []  []          []  []          []  []
[][][][][]  []  [][][]  [][][][][]  [][][][][][][]  [][][][][][][]  []
[]      []  []  []  []              []      []      []          []  []
[]  [][][]  []  []  [][][][][][][][][]  []  []  []  []  [][][]  []  []
[]      []      []                      []  []  []      []      []  []
[]  []  [][][][][][][][][]  [][][]  [][][][][]  [][][][][]  [][][]  []
[]  []      []      []      []      []      []  []      []      []  []
[]  []  []  []  []  []  [][][]  [][][]  []  []  []  []  [][][]  []  []
[]  []  []      []      []      []      []  []  []  []      []      []
[]  []  [][][][][][][][][][][][][]  [][][]  []  []  [][][]  [][][][][]
[]  []          []              []      []      []      []          []
[]  [][][][][]  []  [][][][][]  [][][]  [][][][][][][][][]  [][][]  []
[]      []  []      []              []      []          []      []  []
[][][]  []  [][][][][]  [][][][][]  [][][]  []  [][][]  []  []  [][][]
[]  []      []          []          []      []  []      []  []      []
[]  [][][]  []  []  [][][][][]  [][][]  [][][]  []  [][][][][][][]  []
[]      []  []  []  []      []  []      []      []                  []
[]  [][][]  []  []  []  []  [][][]  [][][][][]  [][][][][][][][][]  []
[]          []  []  []  []      []      []      []      []      []  []
[]  [][][][][]  []  []  [][][]  [][][]  []  [][][]  []  [][][]  []  []
[]  []  []      []  []  []  []      []      []      []          []  []
[]  []  []  [][][]  []  []  []  [][][][][][][][][]  [][][][][][][]  []
[]      []  []  []  []  []  []                      []              []
[][][]  []  []  []  []  []  [][][][][]  [][][]  [][][]  [][][][][][][]
[]      []  []      []  []          []      []  []      []          []
[]  [][][]  [][][][][]  []  [][][]  [][][]  [][][]  [][][][][]  []  []
[]      []                  []          []                      []  []
[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]  []

Donner la longueur du chemin pour arriver le plus rapidement:

Réflexion :
On obtient le labyrinthe qu'il faut résoudre en moins de 3secondes. Il suffit de résoudre le labyrinthe en moins de 3secondes via alogithme type A*.

Solution :
Je suis reparti d'un solveur de labyrinthe : https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc
Il suffit alors de lire chaque ligne du labyrinthe et de remplacer les [] par des 1 et les espaces par des 0.
On demande alors à l'algo de résoudre le labyrinthe et de renvoyer la taille du chemin. On obtient directement le flag :
ESD{HUUUMMMMl@M@Y0avecL3P0ul3t}
