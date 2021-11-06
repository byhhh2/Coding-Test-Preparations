import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())

# N = 운동 해야하는 분
# m = 최소 맥박
# M = 최대 맥박
# T = 운동시 증가
# R = 휴식시 감소 

time = 0
X = m

while True:
    if M - m < T:
        print(-1)
        exit(0)

    time += 1
    if X + T > M:
        if X - R < m:
            X = m
        else:
            X -= R
    else: 
        N -= 1
        X += T
    
    if N <= 0:
        break

print(time)