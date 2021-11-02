import sys

N = int(sys.stdin.readline())
divisor = 2
sieve = []

def isPrime(n):
    global sieve

    if len(sieve) > n:
        return sieve[n]

    sieve = [True] * (n + 1)

    sieve[0] = False
    sieve[1] = False

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    
    return sieve[n]


if N == 1:
    exit(0)
if isPrime(N):
    print(N)
else:
    while not isPrime(N):
        if N % divisor == 0:
            N //= divisor
            print(divisor)
        else:
            while True:
                divisor += 1
                if isPrime(divisor):
                    break
    print(N)