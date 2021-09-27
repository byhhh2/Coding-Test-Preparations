import sys

A, B = map(str, sys.stdin.readline().split())

print(max(int(A[::-1]), int(B[::-1])))