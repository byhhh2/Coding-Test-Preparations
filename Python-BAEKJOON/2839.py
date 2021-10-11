import sys

N = int(sys.stdin.readline())

cnt = 0
tmp = N

while (tmp >= 0):
    if tmp % 5 == 0:
        print(cnt + (tmp // 5))
        exit(0)
    cnt += 1
    tmp -= 3
print(-1)

