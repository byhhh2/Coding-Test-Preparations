# 체스판 칠해칠해

N, M = map(int, input().split())
board = []
cnt1 = 0
cnt2 = 0
min_cnt = 64

str1 = 'WBWBWBWB'
str2 = 'BWBWBWBW'

real_board1 = []
real_board2 = []

for i in range(0, 8):
    if(i % 2 == 0):
        real_board1.append(str1)
        real_board2.append(str2)
    else:
        real_board1.append(str2)
        real_board2.append(str1)

for i in range(0, N):
    tmp_list = input()
    board.append(tmp_list)


for i in range(0, N - 7):
    for j in range(0, M - 7):
        n, m = 0, 0
        cnt1 = 0
        cnt2 = 0
        for k, n in zip(range(i, i + 8), range(0, 8)):
            for l, m in zip(range(j, j + 8), range(0, 8)):
                if (board[k][l] != real_board1[n][m]):
                    cnt1 += 1
                if (board[k][l] != real_board2[n][m]):
                    cnt2 += 1
                m += 1
            n += 1
        if (cnt1 < min_cnt):
            min_cnt = cnt1
        if (cnt2 < min_cnt):
            min_cnt = cnt2

print(min_cnt)
