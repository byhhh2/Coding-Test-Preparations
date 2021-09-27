import sys

N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    flagList = {}
    flag = 0
    input = sys.stdin.readline().rstrip()

    for i in range(1, len(input)):
        if input[i] in flagList:
            flag = 1
            break
        if input[i - 1] != input[i]:
            flagList[input[i - 1]] = 1
    
    if flag == 0:
        cnt += 1

print(cnt)
