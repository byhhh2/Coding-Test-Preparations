import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

last = V - A
day = math.ceil(last / (A - B))

print(day + 1)