import sys
nombre1 = int(sys.stdin.readline())
nombre2 = int(sys.stdin.readline())
nombre3 = int(sys.stdin.readline())
booleen1 = True
booleen2 = True
while booleen1:
    resultat = 0
    for i in map(int,str(nombre1)):
        resultat = resultat + i
    if resultat == nombre3:
        print(resultat)
        booleen1 = False
    else:
        nombre1 += 1
while booleen2:
    resultat = 0
    for i in map(int,str(nombre2)):
        resultat = resultat + i
    if resultat == nombre3:
        print(resultat)
        booleen2 = False
    else:
        nombre2 += 1
