import sys
nbCas = int(sys.stdin.readline())
for i in range(0,nbCas):
    nombres = sys.stdin.readline().split()
    if (int(nombres[0]) - int(nombres[1]) == int(nombres[2]) or int(nombres[1]) - int(nombres[0]) == int(nombres[2])):
        print("Possible")
    elif (int(nombres[0]) + int(nombres[1]) == int(nombres[2]) or int(nombres[1]) + int(nombres[0]) == int(nombres[2])):
        print("Possible")
    elif (int(nombres[0]) * int(nombres[1]) == int(nombres[2]) or int(nombres[1]) * int(nombres[0]) == int(nombres[2])):
        print("Possible")
    elif (int(nombres[0]) / int(nombres[1]) == int(nombres[2]) or int(nombres[1]) / int(nombres[0]) == int(nombres[2])):
        print("Possible")
    else:
        print("Impossible")