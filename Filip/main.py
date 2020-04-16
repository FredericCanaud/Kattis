import sys
nombres = sys.stdin.readline().split()

nombre1 = int(nombres[0])
nombre2 = int(nombres[1])

nombre1 = str(nombre1)[::-1]
nombre2 = str(nombre2)[::-1]

nombre1 = int(nombre1)
nombre2 = int(nombre2)

if nombre1 <= nombre2:
    print(nombre2)
else:
    print(nombre1)
