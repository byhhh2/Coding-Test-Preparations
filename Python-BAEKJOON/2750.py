import sys

N = int(sys.stdin.readline())
input = []

counter = [0] * 10001

for i in range(N):
   counter[int(sys.stdin.readline())] += 1

for i in range(0, 10001):
    if counter[i] != 0:
        for j in range(counter[i]):
            print(i)