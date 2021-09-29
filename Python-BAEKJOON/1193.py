import sys

N = int(sys.stdin.readline())

nextStartNum = 1
cnt = 1

while True:
    if N < nextStartNum:
        realStartNum = nextStartNum - (cnt - 1)
        endNum = nextStartNum - 1

        if (cnt - 1) % 2 == 0 :
            print(f'{N - realStartNum + 1}/{endNum - N + 1}')
        else:
            print(f'{endNum - N + 1}/{N - realStartNum + 1}')
        exit(0)
    else:
        nextStartNum += cnt 
        cnt += 1