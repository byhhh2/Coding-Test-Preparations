import sys

cnt = 0

N = int(sys.stdin.readline())

def isSameDiff(num):
    numList = []

    while num != 0:
        numList.append(num % 10)
        num //= 10

    diffSum = (len(numList) / 2) * (numList[0] + numList[-1])

    if diffSum == sum(numList):
        return True
    else:
        return False

if N < 100:
    print(N)
    exit(0)
else:
    cnt += 99
    n = cnt + 1

    while n <= N:
        if isSameDiff(n):
            cnt += 1
        n += 1

print(cnt)