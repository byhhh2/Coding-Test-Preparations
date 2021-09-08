# 좌표 정렬하기

N = int(input())
xy = []

for i in range(0, N):
    xy.append(list(map(int, input().split())))

xy.sort(key=lambda x: (x[0], x[1]))

for item in xy:
    print(item[0], item[1])
