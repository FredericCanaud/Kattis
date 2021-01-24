cases = [list(map(int, input().split())) for x in range(int(input()))]
taille = len(cases)

# Pour chaque case
for j in range(taille):
    rang = range(cases[j][0], cases[j][1]+1)
    # On réitère pour voir si ça matche
    for i in range(taille):
        rang2 = range(cases[i][0], cases[i][1]+1)
        if cases[i][0] in rang or cases[i][1] in rang:
            continue
        elif cases[j][0] in rang2 or cases[j][1] in rang2:
            continue
        else:
            print("edward is right")
            exit()
print("gunilla has a point")
