import sys
n = int(sys.stdin.readline())
for i in range(0,n):
    line = int(sys.stdin.readline())
    result = 1
    for j in range(2,line+1):
         result = result * j
    print(result % 10)
    

