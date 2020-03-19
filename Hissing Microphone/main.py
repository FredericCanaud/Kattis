import sys
line = sys.stdin.readline()
booleen = True
for i in range(0,len(line)-1):
    if line[i] == 's' and line[i+1] == 's':
        print("hiss")
        booleen = False
        break
if(booleen):
    print("no hiss")