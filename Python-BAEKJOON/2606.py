import sys
sys.setrecursionlimit(10 ** 6)

computerCount = int(sys.stdin.readline())
edgeCount = int(sys.stdin.readline())
virusCount = -1
graph = {}
visited = [False for _ in range(computerCount + 1)]

for i in range(edgeCount):
    a, b = map(int, sys.stdin.readline().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]


def dfs(current):
    global virusCount
    visited[current] = True
    virusCount += 1

    if current not in graph:
        return

    for elem in graph[current]:
        if not visited[elem]:
            dfs(elem)


dfs(1)
print(virusCount)

'''
7
6
1 2
2 3
5 1
5 2
5 6
4 7

=> 반례: 양방향으로 연결해주어야 한다. 

'''
