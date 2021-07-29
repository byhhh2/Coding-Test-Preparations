# 소수의 합과 최솟값

M = int(input())
N = int(input())

sumPrime = 0
minPrime = 0

if (M == 1):
    M += 1

for i in range(M, N+1):
    cnt = 0
    flag = 0
    for j in range(2, i):
        if (i % j == 0):
            flag = 1
            break
    if (flag == 0):
        sumPrime += i
        if(minPrime == 0):
            minPrime = i

if (sumPrime != 0):
    print(sumPrime)
    print(minPrime)
else:
    print(-1)
