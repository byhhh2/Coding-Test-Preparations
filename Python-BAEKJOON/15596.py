import sys

def solve(a):
    return sum(a)

intN = list(map(int, sys.stdin.readline().split()))
print(solve(intN))