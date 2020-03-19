import sys
operations = {'-','+','*','//'}
valeursPossibles = {}

for i in operations:
    for j in operations:
        for k in operations:
            valeurChainee = str(' 4 '+ i + ' 4 ' + j + ' 4 ' + k + ' 4 ')
            valeurEntiere = eval('4'+ i + '4' + j + '4' + k + '4')
            valeursPossibles[valeurEntiere] = valeurChainee.replace('//','/') + " = " + str(valeurEntiere)

nombreCas = int(sys.stdin.readline())
for i in range(0,nombreCas):
    nombre = int(sys.stdin.readline())
    if(nombre in valeursPossibles):
        print(valeursPossibles[nombre])
    else:
        print("no solution")