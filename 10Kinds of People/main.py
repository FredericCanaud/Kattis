import sys


def find(l, x):
    while x != l[x]: x = l[x]
    return x


def unite(l, s, a, b):
    a = find(l, a)
    b = find(l, b)
    if a == b: return
    if s[a] < s[b]: a, b = b, a
    s[a] += s[b]
    l[b] = a

rc = map(int, sys.stdin.readline().split())
r = rc[0]
c = rc[1]
l = [i for i in range(r * c)]
s = [1] * r * c
a = [None] * r
for i in range(r):
    a[i] = list(map(int, sys.stdin.readline().strip().split()))
for i in range(r):
    for j in range(c - 1):
        print(a[i][j])
        if j < c - 1 and a[i][j] == a[i][j + 1]:
            unite(l, s, i * c + j, i * c + j + 1)
        if i < r - 1 and a[i][j] == a[i + 1][j]:
            unite(l, s, i * c + j, (i + 1) * c + j)
for _ in range(input()):
    r1, c1, r2, c2 = [int(x) - 1 for x in sys.stdin.readline().split()]
    if find(l, r1 * c + c1) == find(l, r2 * c + c2):
        if a[r1][c1]:
            print('decimal')
        else:
            print('binary')
    else:
        print('neither')
