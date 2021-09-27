import sys

N = int(sys.stdin.readline())
sum = 0

input = sys.stdin.readline().rstrip()

for i in input:
    sum += int(i)

print(sum)