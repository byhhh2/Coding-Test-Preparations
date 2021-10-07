import sys

N, K = map(int, sys.stdin.readline().split())
index = 0

circle = [i for i in range(1, N + 1)]

print('<', end='')

while N > 0:
    if N > 1:
        print(circle[(index + (K - 1)) % N], end=', ')
    else:
        print(circle[(index + (K - 1)) % N], end='>')
    del circle[(index + (K - 1)) % N]
    index = (index + (K - 1)) % N
    N -= 1

