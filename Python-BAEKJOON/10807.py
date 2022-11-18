import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

count = 0

for elem in L:
    if elem == v:
        count += 1


print(count)
