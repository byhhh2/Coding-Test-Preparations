import sys
from collections import Counter

N = int(sys.stdin.readline())
people_list = []
able_list = []

for i in range(N):
    people_list.append(sys.stdin.readline()[0])

for c in dict(Counter(people_list)):
    if dict(Counter(people_list))[c] >= 5:
        able_list.append(c)

if len(able_list) != 0:
    print(''.join(sorted(able_list)))
else:
    print('PREDAJA')