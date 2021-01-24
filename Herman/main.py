import sys
import math

input = sys.stdin.read()
line = input.strip("\n")
line = line.split()

print("{0:.06f}".format(math.pi * (int(line[0]) ** 2)))
print("{0:.06f}".format((2.0 * (int(line[0]) ** 2))))
