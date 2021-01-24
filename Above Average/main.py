from statistics import mean

for i in range(int(input())):
    x = list(map(int, input().split()))
    x.pop(0)
    moyenne = mean(x)
    print("{0:.3f}%".format(100*len([y for y in x if y > moyenne])/len(x), 3))
