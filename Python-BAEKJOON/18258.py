# 큐 2

import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()
Len = 0

def push(x):
    global Len
    deq.append(x)
    Len += 1

# 삭제할 때 배열의 pop과 deque의 popleft의 시간 차이 발생 
# pop은 배열의 요소를 한칸씩 옮기는 과정이 존재 

def _pop():
    global Len
    if (Len != 0):
        print(deq.popleft())
        Len -= 1
    else:
        print(-1)

def size():
    print(Len)

def empty():
    if Len == 0:
        print(1)
    else:
        print(0)

def front():
    if Len != 0:
        print(deq[0])
    else:
        print(-1)

def back():
    if Len != 0:
        print(deq[-1])
    else:
        print(-1)


for i in range(0, N):
    input = sys.stdin.readline().rstrip().split()

    if input[0] == "push":
        push(input[1])
    elif input[0] == "pop":
        _pop()
    elif input[0] == "size":
        size()
    elif input[0] == "empty":
        empty()
    elif input[0] == "front":
        front()
    elif input[0] == "back":
        back()
