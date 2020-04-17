import sys
heure, minute = sys.stdin.readline().split()
heure = int(heure)
minute = int(minute)
if minute <= 45:
    if heure == 0:
        heure = 23
    else:
        heure = heure - 1
    minute = minute + 15
else:
    minute = minute - 45
print(heure,minute) 