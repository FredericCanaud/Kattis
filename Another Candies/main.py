import sys
nombreCas = int(sys.stdin.readline())
for i in range(0,nombreCas):
    ligneVide = sys.stdin.readline()
    nombreEnfants = int(sys.stdin.readline())
    nombreBonbons = 0
    for j in range(0,nombreEnfants):
        nombreBonbons = nombreBonbons + int(sys.stdin.readline())
    if(nombreBonbons % nombreEnfants == 0):
        print("YES")
    else:
        print("NO")