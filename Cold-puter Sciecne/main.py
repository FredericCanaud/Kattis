import sys
nbCas = int(sys.stdin.readline())
compteur = 0
for i in sys.stdin.readline().split():
    if (int(i) < 0):
        compteur = compteur + 1
print(compteur)