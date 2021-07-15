T = int(input())
cnt = 0
n_array = []

for i in range(0, T):
    n = int(input())
    n_array.append(n)
        
for item in n_array:
    cnt = 0
    while(item != 0):
        if (item % 2 == 1):
            print(cnt, end=' ')
            item //= 2
            cnt += 1
        else:
            item //= 2
            cnt += 1
            continue
    print()