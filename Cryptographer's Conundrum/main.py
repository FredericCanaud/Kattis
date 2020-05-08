import sys
input = sys.stdin.readline()
count = 0
for i in range(1,len(input)-1,3):
    if(input[i-1]=='P'):
        count += 1
    if(input[i]=='E'):
        count += 1
    if(input[i+1]=='R'):
        count += 1
print(len(input) - count)