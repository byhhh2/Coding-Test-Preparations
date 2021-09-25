import sys
from collections import Counter

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

mul = str(A * B * C)

for i in range(0, 10):
    print(mul.count(str(i)))
