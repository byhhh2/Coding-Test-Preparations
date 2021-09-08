# 사탕 게임 0
import sys
from collections import Counter

# N = int(sys.stdin.readline())
# candy_list = []
# tmp_candy_list = []
# cand_max_num = 0
# max_num = 0

# for i in range(0, N):
#     candy_list.append(list(sys.stdin.readline().strip()))

# # print(candy_list)

# tmp_candy_list = candy_list
# # 가로
# for i in range(0, N):
#     for j in range(0, N - 1):
#         tmp_candy_list[i][j], tmp_candy_list[i][j +
#                                                 1] = candy_list[i][j + 1], candy_list[i][j]
#         for k in range(0, N):
#             cand_max_num = Counter(tmp_candy_list[k]).most_common(1)[0][1]
#             for m in range(cand_max_num, 0):
#                 # if ('C' * m not in tmp_candy_list[k] or 'C' * m in tmp_candy_list[k] or 'C' * m in tmp_candy_list[k] or 'C' * m in tmp_candy_list[k]):

#             if (max_num < cand_max_num):
#                 max_num = cand_max_num
#         for k in range(0, N):
#             cand_max_num = Counter([tmp_candy_list[i][k]
#                                    for i in range(0, N)]).most_common(1)[0][1]
#             if (max_num < cand_max_num):
#                 max_num = cand_max_num

#         tmp_candy_list[i][j], tmp_candy_list[i][j +
#                                                 1] = candy_list[i][j + 1], candy_list[i][j]

# # 세로
# for i in range(0, N):
#     for j in range(0, N - 1):
#         tmp_candy_list[j][i], tmp_candy_list[j +
#                                              1][i] = candy_list[j + 1][i], candy_list[j][i]
#         for k in range(0, N):
#             cand_max_num = Counter(tmp_candy_list[k]).most_common(1)[0][1]
#             if (max_num < cand_max_num):
#                 max_num = cand_max_num
#         for k in range(0, N):
#             cand_max_num = Counter([tmp_candy_list[i][k]
#                                    for i in range(0, N)]).most_common(1)[0][1]
#             if (max_num < cand_max_num):
#                 max_num = cand_max_num

#         tmp_candy_list[j][i], tmp_candy_list[j +
#                                              1][i] = candy_list[j + 1][i], candy_list[j][i]

# print(max_num)
