# 제로 
import sys

K = int(sys.stdin.readline())
stack = []

for i in range(0, K):
    _input = int(sys.stdin.readline())

    if (_input == 0):
        stack.pop()
    else:
        stack.append(_input)

print(sum(stack))