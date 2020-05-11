import sys
input = sys.stdin.readline().split()
correct = [1,1,2,2,2,8]
for i in range(0,len(input)):
    input[i] = int(correct[i]) - int(input[i])
print(input[0],input[1],input[2],input[3],input[4],input[5])