# 3번째 큰 수 찾기

A = []
result = []

T = int(input())

for i in range(0, T):
    data = list(map(int, input().split()))
    data.sort()
    result.append(data[-3])


for r in result:
    print(r)
