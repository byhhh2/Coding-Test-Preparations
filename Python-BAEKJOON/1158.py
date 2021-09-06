N, K = map(int, input().split())
_list = []
index = 0
save_N = N

for i in range(1, N + 1):
    _list.append(i)

print('<', end='')
for i in range(0, save_N):
    print(_list[(index + K - 1) % N], end='')
    _list.remove(_list[(index + K - 1) % N])
    index = (index + K - 1) % N
    N -= 1
    if (i != save_N - 1):
        print(', ', end='')

print('>', end='')
