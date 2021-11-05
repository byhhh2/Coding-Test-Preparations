import sys

T = int(sys.stdin.readline())

for t in range(T):
    baseList = []

    a, b = map(int, sys.stdin.readline().split())

    base = a % 10
    if base == 0:
        print(10)
        continue
    
    for i in range(1, 5):
        baseList.append((base ** i) % 10)

    print(baseList[(b % 4) + -1])
