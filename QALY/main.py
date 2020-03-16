import sys
resultat = 0.0
n = int(sys.stdin.readline())
for i in range(0,n):
    line = sys.stdin.readline().split()
    resultat = resultat + float(line[0]) * float(line[1])
print('{:.3f}'.format(resultat))