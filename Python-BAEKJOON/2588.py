import sys

_1 = sys.stdin.readline()
_2 = sys.stdin.readline()
_6 = 0

for i in range(0, 3):
    print(int(_1) * int(_2[2-i]))
    _6 += int(_1) * int(_2[2-i]) * (10 ** i)

print(_6)