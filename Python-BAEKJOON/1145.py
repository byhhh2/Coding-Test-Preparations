from itertools import combinations
import sys
from math import lcm

input = list(map(int, sys.stdin.readline().split()))
outputList = []

for c in combinations(input, 3):
    outputList.append(lcm(c[0], c[1], c[2]))

print(min(outputList))