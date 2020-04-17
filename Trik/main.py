import sys
mouvement = sys.stdin.readline()
position = 1
for i in mouvement:
    if(position == 1):
        if(i == "A"):
            position = 2
        elif(i == "C"):
            position = 3
    elif(position == 2):
        if(i == "A"):
            position = 1
            passage = False
        elif(i == "B"):
            position = 3
    elif(position == 3):
        if(i == "B"):
            position = 2
        elif(i == "C"):
            position = 1
print(position)