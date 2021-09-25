import sys

N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

max =  max(list)
sum = 0

for _ in list:
    _ = _ / max * 100
    sum += _


print(sum / N)