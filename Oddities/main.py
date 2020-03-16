import sys
n = int(sys.stdin.readline())
for i in range(0,n):
    line = int(sys.stdin.readline())
    if line % 2 == 1 :
        print(str(line) + " is odd")
    else:
        print(str(line) + " is even")
