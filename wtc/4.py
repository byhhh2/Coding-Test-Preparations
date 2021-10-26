import sys

def solution(p, c):
    answer = 0

    if p[0] % 2 == 0 or p[1] % 2 == 1:
        return -1
    if c[0] % 2 == 0 or c[1] % 2 == 1:
        return -1
    if p[0] + 1 != p[1]:
        return -1
    if c[0] + 1 != c[1]:
        return -1
    if 1 > p[0] or 400 < p[0] or 1 > p[1] or 400 < p[1]:
        return -1
    if 1 > c[0] or 400 < c[0] or 1 > c[1] or 400 < c[1]:
        return -1 
        

    p_list = []
    c_list = []

    sum = 0
    mul = 1
 
    for i in range(2):
        sum = 0
        mul = 1
        for j in str(p[i]):
            sum += int(j)
            mul *= int(j)
        p_list.append(sum)
        p_list.append(mul)

    for i in range(2):
        sum = 0
        mul = 1
        for j in str(c[i]):
            sum += int(j)
            mul *= int(j)
        c_list.append(sum)
        c_list.append(mul)

    if max(p_list) > max(c_list):
        answer = 1
    elif max(p_list) < max(c_list):
        answer = 2
    elif max(p_list) == max(c_list):
        answer = 0
    else:
        answer = -1


    return answer

while True:
    p_ = list(map(int, sys.stdin.readline().split()))
    c_ = list(map(int, sys.stdin.readline().split()))
    print(solution(p_, c_))