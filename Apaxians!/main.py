import sys
mot = sys.stdin.readline()
mot = list(mot)
motCorrect = []
motCorrect.append(mot[0])
for i in range(0,len(mot)-1):
    if mot[i] != mot[i+1]:
        motCorrect.append(mot[i+1])
print("".join(motCorrect))
