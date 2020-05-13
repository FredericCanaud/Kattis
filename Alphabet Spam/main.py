import sys
mot = sys.stdin.readline()
mot = list(mot)
motCorrect = []
longueur = len(mot)
espaces = 0
symboles = 0
majuscules = 0
minuscules = 0
for i in range(0,len(mot)):
    if ord(mot[i]) == 95:
        espaces = espaces + 1
    elif ( ord(mot[i]) >= 65 and ord(mot[i]) <= 90):
        majuscules = majuscules + 1
    elif ( ord(mot[i]) >= 97 and ord(mot[i]) <= 122):
        minuscules = minuscules + 1
    else:
        symboles = symboles + 1 
print(espaces/longueur)
print(minuscules/longueur)
print(majuscules/longueur)
print(symboles/longueur)
