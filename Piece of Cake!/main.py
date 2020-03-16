import sys
nombres = sys.stdin.readline().split()
nombre1 = int(nombres[0])
nombre2 = int(nombres[1])
nombre3 = int(nombres[2])
if nombre2 < nombre1/2:
    nombre2 = nombre1 - nombre2
if nombre3 < nombre1/2:
    nombre3 = nombre1 - nombre3
print(4*nombre2*nombre3)