abc = list(map(int, input().split()))
abc.sort()

for i in list(input()):
    print(abc[ord(i) % 65], end=' ')
