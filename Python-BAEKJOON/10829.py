import sys

N = int(sys.stdin.readline())

def to_binary(N):
    if N == 1:
        print(1, end='')
        return
    to_binary(N // 2)
    print(N % 2, end='')

to_binary(N)