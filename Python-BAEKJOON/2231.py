# 분해합

N = int(input())
rand = N - 1
flag = 0

while (rand != 0):
    cand_M = N - rand
    save_cand_M = cand_M
    rand -= 1
    M_digit_list = []
    while (cand_M != 0):
        M_digit_list.append(cand_M % 10)
        cand_M //= 10
    if (N == save_cand_M + sum(M_digit_list)):
        flag = 1
        print(save_cand_M)
        exit(0)


if(flag == 0):
    print(0)
