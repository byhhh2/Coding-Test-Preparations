# import sys
# from collections import Counter

# N, d, k, c = map(int, sys.stdin.readline().split())

# sushi_list = []
# cnt_list = []

# for i in range(N):
#     sushi_list.append(int(sys.stdin.readline()))

# for j in range(-N, 0, 1):
#     current_list = []
#     for t in range(j, j+k):
#         current_list.append(sushi_list[t])

#     cnt = len(Counter(current_list))

#     if c in current_list:
#         cnt_list.append(cnt)
#     else:
#         cnt_list.append(cnt + 1)
    

# print(max(cnt_list))

####################

import sys
from collections import Counter
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().split())

sushi_list = []
cnt_list = []
max = 0

for i in range(N):
    sushi_list.append(int(sys.stdin.readline()))


deq = deque(sushi_list[-N:-N+k])
deq.append(c)

length = len(set(deq))

if max < length:
    max = length
    
deq.pop()


for j in range(-N+k, -1+k, 1):
    deq.popleft()
    deq.append(sushi_list[j])
    deq.append(c)

    length = len(set(deq))

    if max < length:
        max = length
    
    deq.pop()

print(max)
