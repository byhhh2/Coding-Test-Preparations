# 소수의 갯수 구하기

N = int(input())
totalCnt = 0

data = list(map(int, input().split()))

for d in data:
    cnt = 0
    if (d == 1):
        continue
    for i in range(1, d):
        if (d % i == 0):
            cnt += 1
    if (cnt == 1):
        totalCnt += 1

print(totalCnt)
