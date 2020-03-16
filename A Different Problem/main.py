import sys
lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    line = line.split()
    nombre1 = line[0]
    nombre2 = line[1]
    print(abs(int(line[0]) - int(line[1])))