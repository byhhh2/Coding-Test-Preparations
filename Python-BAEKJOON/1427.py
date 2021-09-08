# 소트인사이드

N = input()

N_list = list(N)

N_list.sort(reverse=True)

for item in N_list:
    print(item, end='')
