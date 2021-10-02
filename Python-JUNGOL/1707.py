# 달팽이 

import sys

n = int(sys.stdin.readline())

snail = [[0 for col in range(n)] for row in range(n)]
cnt = 1

i = 0
j = 0

while True:
    while j < n and snail[i][j] == 0: # 위
        snail[i][j] = cnt
        cnt += 1
        j += 1
    j -= 1
    i += 1 
    if cnt >= n * n:
        break
    while i < n and snail[i][j] == 0: # 오른
        snail[i][j] = cnt
        cnt += 1
        i += 1
    i -= 1
    j -= 1
    while j >= 0 and snail[i][j] == 0: # 아래
        snail[i][j] = cnt
        cnt += 1
        j -= 1
    j += 1
    i -= 1
    while i >= 0 and snail[i][j] == 0: # 왼
        snail[i][j] = cnt
        cnt += 1
        i -= 1
    j += 1
    i += 1



for s in snail:
    for item in s: 
        print(item, end=' ')
    print()