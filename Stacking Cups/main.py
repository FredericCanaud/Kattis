import sys
dico = {}
resultat = 0.0
n = int(sys.stdin.readline())
for i in range(0,n):
    line = sys.stdin.readline().split()
    if line[0].isdigit():
        dico[line[1]] = int(line[0])/2
    else:
        dico[line[0]] = int(line[1])
resultat = sorted(dico.items(), key=lambda x: x[1])
for i in range(0,n):
    print(resultat[i][0])