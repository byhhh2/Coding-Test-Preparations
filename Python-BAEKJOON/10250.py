import sys

T = int(sys.stdin.readline())

def roomAssign(H, W, N):
    num = 1

    while (N > 0):
        floor = 0

        while (H > floor):
            floor += 1
            N -= 1
            if N <= 0:
                return str(floor) + ('0' + str(num) if (num // 10) == 0 else str(num))
        num += 1
    


for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    print(roomAssign(H, W, N))
    
