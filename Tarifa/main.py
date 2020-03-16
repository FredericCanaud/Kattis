import sys
credit = int(sys.stdin.readline())
n = int(sys.stdin.readline())
budget = credit
for i in range(0,n):
    line = int(sys.stdin.readline())
    budget = budget - line + credit
print(budget)
