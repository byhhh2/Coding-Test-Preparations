import sys

T = int(sys.stdin.readline())

def solution(x, y):
    total_count = 0
    base = 1
    base_count = 0
    distance = y - x
    remainder = 0
    
    while True:
        if base * base > distance:
            base -= 1
            base_count = (base * 2) - 1
            break
        base += 1

    total_count += base_count
    remainder = distance - (base * base)

    while True:
        if remainder - base >= 0:
            total_count += 1
            remainder -= base   
        else:
            base -= 1
        if remainder == 0:
            return total_count


for t in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print(solution(x, y))