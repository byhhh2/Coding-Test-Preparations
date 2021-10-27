import sys

input = []

N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    input.append(list(map(int, sys.stdin.readline().rstrip())))

def DFS(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if input[x][y] == 0:
        input[x][y] = 1 # 방문 처리 

        DFS(x - 1, y) # 상
        DFS(x + 1, y) # 하
        DFS(x, y - 1) # 좌
        DFS(x, y + 1) # 우
        return True

    return False

count = 0

for i in range(N):
    for j in range(M):
        if DFS(i, j):
            count += 1

print(count)

'''
4 5
00110
00011
11111
00000

> 3
'''