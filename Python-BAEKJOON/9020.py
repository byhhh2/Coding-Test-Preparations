import sys

T = int(sys.stdin.readline())
sieve = [True] * (10000 + 1)

def search_partition(n):
    a = 0
    b = 0 
    diff = n

    prime_list = current_prime(n)

    if n // 2 in prime_list:
        print(n // 2, n // 2)
        return

    for p in prime_list:
        if sieve[n - p]:
            if diff > abs((n - p) - p):
                a = p
                b = n - p
                diff = abs(a - b)
    
    print(a, b)


def is_prime(end):
    global sieve
    
    _end = int(end ** 0.5)
    for i in range(2, _end + 1):
        if sieve[i] == True:
            for j in range(i + i, end + 1, i):
                sieve[j] = False

def current_prime(end):
    return [i for i in range(2, end + 1) if sieve[i] == True]


for i in range(T):
    n = int(sys.stdin.readline())
    is_prime(10000)
    search_partition(n)