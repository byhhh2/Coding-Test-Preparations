import sys

maze = []
count = 0

def DFS(x, y):
    global count

    if x >= N or y >= M:
        return 0

    if x == N - 1 and y == M - 1:
        count += 1
        return 1

    if maze[x][y] == 1:
        count += 1
        maze[x][y] = 0
        
        DFS(x + 1, y)
        DFS(x, y + 1)
    
    return 0


N, M = map(int, sys.stdin.readline().split())

for i in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

DFS(0, 0)
print(count)

'''
5 6
101010
111111
000001
111111
111111

5 6
111010
111111
000001
111111
111111
- 이 경우를 제외하는 듯 

3 3
110
010
011
'''