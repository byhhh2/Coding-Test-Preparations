from functools import wraps
import sys

def is90(a, b, c):
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    is90(a, b, c)
