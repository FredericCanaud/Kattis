import sys
data = sys.stdin.readline().split()
nbPersonnesAutorises = int(data[0])
nbCas = int(data[1])
nbPersonnesPresentes = 0
nbGroupesRefuses = 0
for i in range(0,nbCas):
    data = sys.stdin.readline().split()
    mouvement = str(data[0])
    nbPersonnes = int(data[1])
    if(mouvement == "enter"):
        if(nbPersonnes + nbPersonnesPresentes <= nbPersonnesAutorises):
            nbPersonnesPresentes = nbPersonnesPresentes + nbPersonnes
        else:
            nbGroupesRefuses = nbGroupesRefuses + 1
    else:
        nbPersonnesPresentes = nbPersonnesPresentes - nbPersonnes
print(nbGroupesRefuses)