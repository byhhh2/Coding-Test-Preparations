# 스택 

import sys

stack = []

def _push(x):
    stack.append(x)

def _pop():
    if (len(stack) > 0):
        print(stack.pop())
    else:
        print(-1)

def _size():
    print(len(stack))

def _empty():
    if (len(stack) > 0):
        print(0)
    else:
        print(1)

def _top():
    if(len(stack) > 0):
        print(stack[-1])
    else:
        print(-1)

N = int(sys.stdin.readline())

for i in range(0, N):
    line = list(sys.stdin.readline().split())
    
    if(line[0] == "push"):
        _push(int(line[1]))
    elif(line[0] == "pop"):
        _pop()
    elif(line[0] == "size"):
        _size()
    elif(line[0] == "empty"):
        _empty()
    elif(line[0] == "top"):
        _top()
