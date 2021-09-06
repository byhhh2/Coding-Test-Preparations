# 블랙잭

import itertools

N, M = map(int, input().split())
card_list = (list(map(int, input().split())))
max_num = 0

combinations_list = itertools.combinations(card_list, 3)
list_ = (list(combinations_list))

for item in list_:
    if (sum(item) > max_num and sum(item) <= M):
        max_num = sum(item)

print(max_num)
