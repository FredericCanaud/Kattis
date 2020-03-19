import sys
nombre = int(sys.stdin.readline())
resultat = 2
for i in range(0,nombre):
    resultat = resultat + 2**i
print(resultat*resultat)