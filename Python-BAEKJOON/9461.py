import sys

T = int(sys.stdin.readline())

def P(n):
    p_arr = [1, 1, 1]
    for i in range(3, n + 1):
        p_arr.append(p_arr[i-3] + p_arr[i-2])
    print(p_arr[n - 1])

for i in range(T):
    N = int(sys.stdin.readline())
    P(N)