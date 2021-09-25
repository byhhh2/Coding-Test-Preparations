import sys
from collections import Counter

list = []
cnt = []

for i in range(10):
    list.append(int(sys.stdin.readline()) % 42)
    cnt = Counter(list)

print(len(cnt))