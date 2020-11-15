#!/usr/bin/python3
# coding: utf-8

grille = [
[0, 8, 0, 0, 4, 7, 9, 0, 0], # lst 0 [ elt 0, elt ..., elt, elt i, elt, elt, elt, elt, elt n]
[0, 0, 0, 6, 8, 2, 0, 0, 4], # lst ...
[0, 5, 4, 0, 0, 0, 0, 0, 0],

[5, 9, 3, 0, 0, 8, 0, 1, 6], # lst i
[0, 7, 2, 0, 0, 0, 4, 3, 0],
[4, 6, 0, 1, 0, 0, 5, 9, 2],

[0, 0, 0, 0, 0, 9, 8, 6, 0],
[6, 0, 0, 8, 1, 4, 0, 0, 0],
[0, 0, 9, 7, 3, 0, 0, 4, 0] # lst n
]

def affichageDeLaGrille ():
  i = 0 # Compteur de listes (lst)
  j = 0 # Compteur d’éléments (elt)
  for lst in grille:
    if (i%3 == 0):
      print (end='\n') # On insère une ligne vide toutes les 3 lignes.
    for elt in lst:
      if (j%3 == 0):
        print (' ', end=' ') # On insère un espace toutes les 3 éléments.
      print(elt, end='')
      j += 1
    print (end='\n') # On affiche une nouvelle ligne, donc on l‘“imprime” sur une nouvelle ligne de l’écran.
    i += 1

def valeursProbables (x, y):
  ROW = [x for x in grille[x]] # Sélectionne toutes les valeurs sur la ligne n°x
  COL = [r[y] for r in grille] # Sélectionne toutes les valeurs sur la colonne n°y.
  SQU = [grille[X][Y] # Sélectionne toutes les valeurs du bloc de la cellule sur la ligne n° x et sur la colonne n°y.
    for X in range (x//3 * 3, x//3 * 3 + 3)
    for Y in range (y//3 * 3, y//3 * 3 + 3)]
  return set(range(1, 10)) - set(ROW + COL + SQU)


def estValide (position):
  if (position == 81): # Si on a atteint la dernière position de la grille.
    return True # on retourne True à l’appelant.
  # Traduction  de sa position en coordonnées :
  i = position // 9 # la partie entière de la division par 9 donne l’abscisse,
  j = position % 9 # le reste de sa division par 9 donne l’ordonnée.

  if (grille[i][j] != 0): # Le chiffre à cette position n’est pas à trouver : on continue avec le suivant.
    return estValide (position+1) # par un appel récurrent.

  for valeurs in valeursProbables (i, j):
    grille[i][j] = valeurs # On teste cette valeur probable (probabilité non nulle). Ici en l’affectant à la grille.
    if (estValide (position+1)): # Peut-on trouver des valeurs aux positions suivantes jusqu’à la 81 ?
      return True # Si oui, on le signale en renvoyant True à l’appelant.
    else:
      grille[i][j] = 0 # Sinon, on remet à zéro la valeur à cet emplacement.
  return False # Après avoir testé toutes les valeurs probables, c’est un échec et on le signale en renvoyant False à l’appelant.

if (__name__ == '__main__'): # renvoie True si il ne s'agit pas d'un module.
  print ('\nGrille initiale, les zéros correspondent aux valeurs à rechercher.')
  affichageDeLaGrille ()
  if estValide (0):
    print ('\n\nGrille finale :')
    affichageDeLaGrille()
  else:
    print ("Cette grille n’a pas de solutions.") # Toutes les solutions possibles ont été testées.
