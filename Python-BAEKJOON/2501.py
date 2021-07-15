p, q = input().split()
p = int(p)
q = int(q)
flag = 0

cnt = 0
i = 1

for i in range(1, p + 1):
    if (p % i != 0):
        continue
    else:
        cnt += 1
        if (cnt == q):
            flag = 1
            print(i)
            break

if (flag == 0):
    print(0)
