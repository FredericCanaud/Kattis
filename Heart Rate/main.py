import sys
nbCas = int(sys.stdin.readline())
for i in range(0,nbCas):
    data = sys.stdin.readline().split()
    battements = int(data[0])
    secondes = float(data[1])
    t = 60 / secondes
    bpm = (60 * battements) / secondes
    print('{0:5f}'.format(bpm-t),'{0:5f}'.format(bpm),'{0:5f}'.format(bpm+t))