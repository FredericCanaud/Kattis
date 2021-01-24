import sys

livres = sorted(sys.stdin.read().split("\n")[1:-1], key=int, reverse=True)
panier = ([livres[i:i + 3] for i in range(0, len(livres), 3)])
total = 0
for livre in panier:
    livre = [int(x) for x in livre]
    if len(livre) == 3:
        total += (sum(livre) - min(livre))
    else:
        total += sum(livre)
print(total)
