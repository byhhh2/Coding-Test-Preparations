# import sys

# M, N = map(int, sys.stdin.readline().split())

# for num in range(M, N + 1):
#     flag = False 

#     for i in range(2, num):
#         if num % i == 0:
#             flag = True
#             break
    
#     if flag == False:
#         print(num)

import sys

def isPrime(start, end):
    sieve = [True] * (end + 1)
    sieve[1] = False

    m = int(end ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, end + 1, i): 
                sieve[j] = False

    [print(i) for i in range(start, end + 1) if sieve[i] == True]


M, N = map(int, sys.stdin.readline().split())
isPrime(M, N)