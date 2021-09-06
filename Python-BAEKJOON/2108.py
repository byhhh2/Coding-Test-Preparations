N = int(input())
num_list = []
mode = []
cnt = 0

for i in range(0, N):
    tmp = int(input())
    num_list.append(tmp)


# 산술평균
avg = round(sum(num_list) / N)
print(avg)

# 중앙값
num_list.sort()
print(num_list[N // 2])

# 최빈값
for i in range(0, N):
    if (num_list[i] not in [item[0] for item in mode]):
        mode.append([num_list[i], 1])
    else:
        for item in mode:
            if (item[0] == num_list[i]):
                item[1] += 1

# print(mode)
mode.sort(key=lambda x: (-x[1], x[0]))
# print(mode)
if (len(mode) > 1 and mode[0][1] == mode[1][1]):
    print(mode[1][0])
else:
    print(mode[0][0])

# 범위
print(num_list[N-1] - num_list[0])
