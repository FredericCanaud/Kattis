import sys
import math

nombres = sys.stdin.readline().split()
nombre1 = int(nombres[0])
nombre2 = int(nombres[1])
nombre3 = int(nombres[2])
for i in range(0,nombre1):
    line = int(sys.stdin.readline())
    if(math.sqrt(nombre2*nombre2 + nombre3*nombre3) >= line):
        print("DA")
    else:
        print("NE")