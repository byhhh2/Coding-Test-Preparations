import sys

def solution(number):
    answer = 0

    for i in range(1, number + 1):
        for j in str(i):
            if '3' in j:
                answer += 1
            if '6' in j:
                answer += 1
            if '9' in j:
                answer += 1

    return answer

num = int(sys.stdin.readline())
print(solution(num))