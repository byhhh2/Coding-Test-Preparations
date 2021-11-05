import sys

x, y, w, h = map(int, sys.stdin.readline().split())

lengthList = []

lengthList.append(x)
lengthList.append(y)
lengthList.append(w - x)
lengthList.append(h - y)

print(min(lengthList))