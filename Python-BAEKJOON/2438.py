import sys

N = int(sys.stdin.readline())

for _ in range(1, N+1):
    print(' ' * (N - _), end='')
    print('*' * _)