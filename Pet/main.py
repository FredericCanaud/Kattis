import sys
topScore = 0
position = 1
for i in range(0,5):
    score = 0
    input = sys.stdin.readline().split()
    for j in range(0,4):
        score += int(input[j])
    if topScore < score:
        position = i+1
        topScore = score
print(position,topScore)