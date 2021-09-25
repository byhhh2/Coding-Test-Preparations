import sys

def calScore(input):
    cnt = 0
    total = 0
    for i in input:
        if i == 'O':
            cnt += 1
        else:
            cnt = 0
        total += cnt
    print(total)

T = int(sys.stdin.readline())

for _ in range(T):
    input = sys.stdin.readline()
    calScore(input)