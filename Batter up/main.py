import sys
nbJeu = int(sys.stdin.readline())
compteur = 0
for i in sys.stdin.readline().split():
    if int(i) == -1:
        nbJeu = nbJeu - 1
    else:
        compteur = compteur + int(i)
print(compteur/nbJeu)