import sys

def sum_prime(n):
    start = n + 1
    end = 2 * n
    print(is_prime(start, end))

def is_prime(start, end):
    total_count = 0
    sieve = [True] * (end + 1)
    sieve[1] = False

    _end = int(end ** 0.5)
    for i in range(2, _end + 1):
        if sieve[i] == True:
            for j in range(i + i, end + 1, i):
                sieve[j] = False

    for i in range(start, end + 1):
        if sieve[i] == True:
            total_count += 1

    return total_count

while True:
    input = int(sys.stdin.readline())
    if input == 0:
        break
    sum_prime(input)
