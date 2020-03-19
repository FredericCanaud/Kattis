import sys
nombreCas = int(sys.stdin.readline())
resultat = 0
for i in range(0,nombreCas):
    entree = int(sys.stdin.readline())
    nombre = entree // 10
    exposant = entree % 10
    resultat = resultat + nombre**exposant
print(resultat*resultat)