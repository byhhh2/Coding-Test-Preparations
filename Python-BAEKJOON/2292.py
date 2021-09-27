import sys 

N = int(sys.stdin.readline())
cycle = 1
cnt = 1

while True:
    if N <= cycle:
        print(cnt) 
        exit(0)

    cycle += 6 * cnt
    cnt += 1