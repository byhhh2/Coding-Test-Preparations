import sys

N = int(sys.stdin.readline())

cnt = 0

if N % 5 == 0:
    print(N // 5)
elif (N % 5) % 3 == 0:
    print((N // 5) + ((N % 5) // 3))
else:
    if (N % 5) % 3 != 0:
        tmp = N
        while (tmp > 0):
            cnt += 1
            tmp -= 3
            if tmp % 5 == 0:
                print(cnt + (tmp // 5))
                exit(0)
        print(-1)

