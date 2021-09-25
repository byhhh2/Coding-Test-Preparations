import sys

def printAvg(n, input):
    avg = sum(input) / n
    cnt = 0 

    for i in input:
        if i > avg:
            cnt += 1
  
    print(f'{cnt / n * 100:.3f}%')
        

C = int(sys.stdin.readline())

for _ in range(C):
    input = list(map(int, sys.stdin.readline().split()))
    printAvg(input[0], input[1: input[0] + 1])

