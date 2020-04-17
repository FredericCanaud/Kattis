import sys
xa, ya = sys.stdin.readline().split()
xb, yb = sys.stdin.readline().split()
xc, yc = sys.stdin.readline().split()

if(xa == xb):
    xd = xc
elif(xa == xc):
    xd = xb
else:
    xd = xa

if(ya == yb):
    yd = yc
elif(ya == yc):
    yd = yb
else:
    yd = ya

print(xd,yd)