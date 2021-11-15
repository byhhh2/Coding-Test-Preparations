import sys
from collections import Counter

point_list_x = []
point_list_y = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    point_list_x.append(x)
    point_list_y.append(y)

print(Counter(point_list_x).most_common()[1][0], Counter(point_list_y).most_common()[1][0])