import sys

def solution(money):
    answer = []
    unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]

    for u in unit:
        answer.append(money // u)
        money %= u
    

    return answer

input = int(sys.stdin.readline())
print(solution(input))