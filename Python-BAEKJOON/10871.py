import sys

N, X = map(int, sys.stdin.readline().split())
input = list(map(int, sys.stdin.readline().split()))


for i in input:
    if i < X:
        print(i, end=' ')