# DFS

<br>

| 동작 원리 | 구현 방법 |
| :-------: | :-------: |
|   스택    |   재귀    |

<br>

- 깊이 우선 탐색
- 깊은 부분을 우선적으로 탐색한다.

<br>

### 동작 과정

<br>

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리한다.
2. 스택의 top에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 top을 꺼낸다.
3. `2`번 과정 반복

<br>

### 구현

<br>

> 스택에 기초하지만 스택을 쓰지 않고 구현할 수 있다. `o(N)`

```python

def DFS(graph, v, visited):
    visited[v] = True # 현재 노드 방문 처리
    print(v, end=' ')

    # 현재 노드의 인접 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

DFS(graph, 1, visited)

```

<br>
<br>

# BFS

<br>

| 동작 원리 | 구현 방법 |
| :-------: | :-------: |
|    큐     |  큐 이용  |

<br>

- 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘
- 일반적인 수행시간이 DFS보다 빠르다.

<br>

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모듀 큐에 삽입하고 방문 처리한다.
3. `2`번 과정 반복

<br>

```python

from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])

    visited[start] = True # 현재 노드 방문 처리

    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() # 큐에서 원소 하나를 뽑아 출력
        print(v, end=' ')

        for i in graph[v]: # v의 인접 노드중 방문하지 않은 노드를 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9

BFS(graph, 1, visited)

```

<br>
<br>

- 참고도서 - 이것이 코딩테스트다
