import sys
while True:
    jack, jill = [int(i) for i in sys.stdin.readline().split()]
    if int(jack) == 0 and int(jill) == 0:
        break
    else:
        jackList =set(int(sys.stdin.readline()) for _ in range(jack))
        jillList =set(int(sys.stdin.readline()) for _ in range(jill))
        diff = jackList&jillList
        print(len(diff))