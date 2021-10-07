import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque([i for i in range(1, N + 1)])
flag = 0


while len(deq) > 1:
    if flag == 0:
        deq.popleft()
        flag = 1
    else:
        deq.append(deq[0])
        deq.popleft()
        flag = 0

print(deq[0])