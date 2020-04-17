import sys
cout = float(sys.stdin.readline())
parcelles = int(sys.stdin.readline())
coutTotal = 0
for i in range(0,parcelles):
    nombres = sys.stdin.readline().split()
    longueur = float(nombres[0])
    largeur = float(nombres[1])
    coutTotal  = coutTotal + longueur*largeur*cout
print('{0:.7f}'.format(coutTotal))