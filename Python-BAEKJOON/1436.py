N = int(input())
end = '666'

for i in range(0, N):
    tmp_i = i
    tmp_list = []
    while (tmp_i != 0):
        tmp_list.append(tmp_list % 10)
        tmp_i /= 10

    cand = str(i) + end

print(cand)
