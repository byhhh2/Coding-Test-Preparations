import sys

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

front = (N // 100) * 100
cnt = 1

if front % F == 0:
     print('{0:02}'.format(front % 100))
else:
    while True:
        if (front + cnt) % F == 0:
            print('{0:02}'.format((front + cnt) % 100))
            exit(0)
        else:
            cnt += 1