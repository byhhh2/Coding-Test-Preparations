import sys

N = int(sys.stdin.readline())
saveN = N
cycle = 0

while True:
    cycle += 1
    mid = (N // 10) + (N % 10) 
    newNum = (N % 10) * 10 + (mid % 10)
    if newNum == saveN:
        print(cycle)
        exit(0)
    N = newNum