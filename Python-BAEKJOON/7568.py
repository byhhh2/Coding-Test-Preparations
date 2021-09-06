# 덩치

N = int(input())
body_list = []

for i in range(0, N):
    tmp_list = list(map(int, input().split()))
    tmp_list.append(i)
    tmp_list.append(1)
    body_list.append(tmp_list)

tmp_body_list = body_list
tmp_body_list.sort(key=lambda x: (-x[0], -x[1]))

for i in range(0, N):
    for j in range(i + 1, N):
        std_w = tmp_body_list[i][0]
        std_h = tmp_body_list[i][1]

        if(std_w > tmp_body_list[j][0] and std_h > tmp_body_list[j][1]):
            tmp_body_list[j][3] += 1

tmp_body_list.sort(key=lambda x: x[2])

for i in range(0, N):
    print(tmp_body_list[i][3], end=' ')
