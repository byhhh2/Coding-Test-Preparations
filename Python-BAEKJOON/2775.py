import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline()) #층
    n = int(sys.stdin.readline()) #호수

    apt = [[_ for _ in range(1, n + 1)]]

    for i in range(k):
        new = []
        for j in range(n):
            new.append(sum(apt[i][0:j + 1]))
        apt.append(new)
    
    print(apt[k][n - 1])

    

# import sys
# import math

# T = int(sys.stdin.readline())

# for _ in range(T):
#     k = int(sys.stdin.readline()) #층
#     n = int(sys.stdin.readline()) #호수
    
#     print(math.comb(k+n, n-1))

    
