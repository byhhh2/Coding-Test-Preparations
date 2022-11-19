import sys

N = sys.stdin.readline().strip()
nums = [int(num) for num in N]
set = [0 for _ in range(10)]
buyCount = 0

for num in nums:
    if set[num] > 0:
        set[num] -= 1
    elif num == 9 and set[6] > 0:
        set[6] -= 1
    elif num == 6 and set[9] > 0:
        set[9] -= 1
    else:
        buyCount += 1
        set = list(map(lambda x: x + 1, set))
        set[num] -= 1

print(buyCount)
