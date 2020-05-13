import sys
modulo = set()
for i in range(10):
    modulo.add(int(sys.stdin.readline()) % 42)
print(len(modulo))