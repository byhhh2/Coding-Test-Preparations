# 문자마름모

import sys

N = int(sys.stdin.readline())

alphabet = [ord('A') + i for i in range(0, 27)]
rhombus = [[0 for col in range(2 * N - 1)] for row in range(2 * N - 1)]


cnt = 0

i = 0
j = (2 * N - 1) // 2


endCnt = 0
rowCnt = 1 

for _ in range(0, N):
    if (_ == N -1):
        endCnt += rowCnt
        break
    endCnt += rowCnt * 2
    rowCnt += 2
    
for q in range((2 * N - 1) // 2): 
    for w in range(((2 * N - 1) // 2) - q):
        rhombus[q][w] = -1
        rhombus[q][(2 * N - 1) - w - 1] = -1
    
q = (2 * N - 1) // 2 + 1

for e in range(q, (2 * N - 1)):
    for w in range(0,  e - ((2 * N - 1) // 2)):
        rhombus[e][w] = -1
        rhombus[e][(2 * N - 1) - w - 1] = -1


while True:
    while j >=0 and rhombus[i][j] == 0:
        rhombus[i][j] = alphabet[cnt % 26]
        cnt += 1
        j -= 1
        i += 1
    j += 2  
    if cnt >= endCnt - 1:
        break
    while i < 2 * N - 1 and rhombus[i][j] == 0:
        rhombus[i][j] = alphabet[cnt % 26]
        cnt += 1
        j += 1
        i += 1
    i -= 2
    while j < 2 * N - 1 and rhombus[i][j] == 0:
        rhombus[i][j] = alphabet[cnt % 26]
        cnt += 1
        j += 1
        i -= 1
    j -= 2
    while i >= 0 and rhombus[i][j] == 0:
        rhombus[i][j] = alphabet[cnt % 26]
        cnt += 1
        i -= 1
        j -= 1
    i += 1

for r in rhombus:
    for item in r: 
        if item == -1:
            print(' ' ,end=' ')
        else:
            print(chr(item), end=' ')
    print()

