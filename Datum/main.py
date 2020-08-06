import sys
input = sys.stdin.readline().split()
answer = 0
nbDaysMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ['Thursday','Friday','Saturday','Sunday','Monday','Tuesday','Wednesday']
for i in range(0,int(input[1])-1):
    answer += nbDaysMonth[i]
print(days[(answer + int(input[0])-1) % len(days)])