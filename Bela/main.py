import sys
sansAtout = {'7': 0, '8': 0, '9': 0, 'T': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
avecAtout = {'7': 0, '8': 0, '9': 14, 'T': 10, 'J': 20, 'Q': 3, 'K': 4, 'A': 11}

data = sys.stdin.readline().split()
nbJeu = int(data[0])
atout = str(data[1])
nbPoints = 0
for i in range(0,nbJeu*4):
    mot = sys.stdin.readline()
    if mot[1] == atout:
        nbPoints = nbPoints + avecAtout[mot[0]]
    else:
        nbPoints = nbPoints + sansAtout[mot[0]]
print(nbPoints)