import sys
lastTime = 0
distance = 0
while True:
    nbSpeeds = int(sys.stdin.readline())
    if (nbSpeeds == -1):
        break
    else:
        for j in range(0,nbSpeeds):
            speed, time = sys.stdin.readline().split()
            distance += int(speed) * (int(time) - lastTime)
            lastTime = int(time)
        print(distance,"miles")
        distance = 0
        lastTime = 0
