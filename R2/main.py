import sys
nombres = sys.stdin.readline().split()
nombre1 = int(nombres[0])
nombre2 = int(nombres[1])
if(nombre2 > nombre1):
    print(nombre2 + nombre2 - nombre1)
else:
    print(nombre2 - (nombre1 - nombre2))