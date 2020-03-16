import sys
nombres = sys.stdin.readline().split()
nombre1 = int(nombres[0])
nombre2 = int(nombres[1])
nombre3 = int(nombres[2])
for i in range(1,nombre3+1):
    if i % nombre1 == 0:
        if i % nombre2 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if i % nombre2 == 0:
            print("Buzz")
        else:
            print(i)