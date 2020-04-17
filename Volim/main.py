import sys
joueur = int(sys.stdin.readline())
nbQuestions = int(sys.stdin.readline())
tempsEcoule = 0
for i in range(0,nbQuestions):
    data = sys.stdin.readline().split()
    temps = int(data[0])
    reponse = str(data[1])
    tempsEcoule += temps
    if(tempsEcoule < 210):
        if reponse == 'T':
            if joueur == 8:
                joueur = 1
            else:
                joueur = joueur + 1
        else:
            continue
    else:
        break
print(joueur)