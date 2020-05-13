import sys
word = sys.stdin.readline().split()
words = []
same = True
for i in word:
    if i not in words:
        words.append(i)
    else:
        print("no")
        same = False
        break
if same:
    print("yes")