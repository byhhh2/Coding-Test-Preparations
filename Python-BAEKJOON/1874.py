# 스택 수열

import sys

input = []
stack = []
num = 1
op = []


N = int(sys.stdin.readline())

for i in range(0, N):
    input.append(int(sys.stdin.readline()))


for i in range(0, N):
    while(1):
        if (len(stack) != 0 and stack[-1] == input[i]):
            stack.pop()
            op.append('-')
            break
        elif (len(stack) == 0 or stack[-1] < input[i]):
            stack.append(num)
            num += 1
            op.append('+')
        else:
            print('NO')
            exit(0)


for i in op:
    print(i)