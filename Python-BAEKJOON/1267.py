import sys


N = int(sys.stdin.readline())
calls = list(map(int, sys.stdin.readline().split()))

Y = 0
M = 0

for call in calls:
    Y_call_count = call // 30 + 1
    M_call_count = call // 60 + 1

    Y += Y_call_count * 10
    M += M_call_count * 15

if Y > M:
    print('M', M)
elif M > Y:
    print('Y', Y)
else:
    print('Y M', Y)
