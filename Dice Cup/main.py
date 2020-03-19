import sys
nombres = sys.stdin.readline().split()
nombre1 = int(nombres[0])
nombre2 = int(nombres[1])
if nombre1 < nombre2:
    for i in range(nombre1+1,nombre2+2):
        print(i)
elif nombre2 < nombre1:
    for i in range(nombre2+1,nombre1+2):
        print(i)
else:
    print(nombre1+1)