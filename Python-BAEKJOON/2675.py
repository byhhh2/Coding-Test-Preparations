import sys

T = int(sys.stdin.readline())


for i in range(T):
    R, S = map(str, sys.stdin.readline().split())

    for s in S:
        for k in range(int(R)):
            print(s, end='')
    print()


