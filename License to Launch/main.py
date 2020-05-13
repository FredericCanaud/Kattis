import sys
nbJours = sys.stdin.readline()
junks = sys.stdin.readline().split()
minJunk = 100000000000
position = 0
for i in range(0,len(junks)):
    if minJunk > int(junks[i]):
        minJunk = int(junks[i])
        position = i
print(position)