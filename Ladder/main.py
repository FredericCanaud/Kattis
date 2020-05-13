import math, sys
h, v = (int(s) for s in sys.stdin.readline().split())
vrad = (v * 3.1415926549)/180
print(int(math.ceil(h/math.sin(vrad))))