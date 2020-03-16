import sys
line = sys.stdin.readline().split('-')
resultat = ''
for i in line:
    char = i[0]
    resultat = resultat + char
print(resultat)