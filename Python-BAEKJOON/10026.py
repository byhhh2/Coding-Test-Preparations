import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
painting = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
partitionCount, blindnessPartitionCount = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue

        if not visited[nx][ny] and painting[nx][ny] == painting[x][y]:
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            partitionCount += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    painting[i] = painting[i].replace('G', 'R')


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j)
            blindnessPartitionCount += 1


print(partitionCount, blindnessPartitionCount)
