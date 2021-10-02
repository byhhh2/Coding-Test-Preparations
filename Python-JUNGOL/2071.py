# 파스칼 삼각형

import sys

n, m = map(int, sys.stdin.readline().split())

pascal = []
cnt = 0

pascal.append([1])

for p in pascal:
    newList = []
    newList.append(1)
    for i in range(0, len(p) - 1):
        newList.append(p[i] + p[i + 1])
    newList.append(1)
    pascal.append(newList)
    cnt += 1
    if cnt == n-1:
        break


if m == 1:
    for p in pascal:
        for item in p:
            print(item, end=' ')
        print()
elif m == 2:
    for i in range(len(pascal)-1, -1, -1):
        for j in range(len(pascal) - len(pascal[i])):
            print(' ', end='')
        for k in range(len(pascal[i])):
            print(pascal[i][k], end=' ')
        print()
elif m == 3:
    for i in range(len(pascal)-1, -1, -1):
        for j in range(len(pascal)-1, i - 1, -1):
            print(pascal[j][i], end=' ')
        print()
