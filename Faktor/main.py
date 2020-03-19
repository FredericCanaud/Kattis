import sys
nombres = sys.stdin.readline().split()
nombre1 = int(nombres[0])
nombre2 = int(nombres[1])
print(int(nombre1*nombre2-nombre1+1))