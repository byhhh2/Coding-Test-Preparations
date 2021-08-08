# 빗물

H, W = map(int, (input().split()))
block_array = list(map(int, input().split()))
result = 0

row_block_return = []


def find_block(row_array):
    row_block_array = []
    for i in range(0, W):
        if (row_array[i] == -1):
            row_block_array.append(i)
    return row_block_array


_2array = [[0] * W for _ in range(H)]

for i in range(0, W):
    for j in range(H - 1, H - block_array[i] - 1, -1):
        _2array[j][i] = -1


for i in range(0, H):
    row_block_return = find_block(_2array[i])
    for j in range(0, len(row_block_return) - 1):
        for k in range(row_block_return[j] + 1, row_block_return[j+1]):
            _2array[i][k] = 1
            result += 1


print(result)
