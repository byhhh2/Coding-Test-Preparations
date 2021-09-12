# 괄호 

import sys

def isVPS(input):
    stack = []
    for i in input:
        if (i == '('):
            stack.append(i)
        else:
            if (len(stack) > 0):
                stack.pop()
            else:
                print("NO")
                return

    if (len(stack) > 0):
        print("NO")
    else:
        print("YES")

T = int(sys.stdin.readline())

for i in range(0, T):
    isVPS(sys.stdin.readline().strip())