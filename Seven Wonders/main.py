import sys
points = 0
nombreT = 0
nombreG = 0
nombreC = 0
lettres = sys.stdin.readline()
for lettre in lettres:
    if lettre == 'T':
        nombreT += 1
    elif lettre == 'G':
        nombreG += 1
    else:
        nombreC += 1
points += nombreC * nombreC + nombreG * nombreG + nombreT * nombreT
while( (nombreC > 0) and (nombreG > 0) and (nombreT > 0) ):
    points += 7
    nombreT -= 1
    nombreG -= 1
    nombreC -= 1
print(points)