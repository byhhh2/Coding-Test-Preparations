import sys
from typing import Pattern

N = int(sys.stdin.readline())
strList = []

for i in range(N):
    strList.append(sys.stdin.readline().rstrip())

pattern = []
flag = 0

if N == 1:
    print(strList[0])
    exit(0)

for i in range(len(strList[0])):
    flag = 0
    for j in range(N - 1):
        if strList[j][i] != strList[j + 1][i]:
            pattern.append('?')
            flag = 1
            break
    if flag == 0:
        pattern.append(strList[j - 1][i])
    
print(''.join(pattern))