import sys

N, M, L = map(int, sys.stdin.readline().split())


current = 0
peoples = []

for i in range(N):
    peoples.append(i)

game = dict.fromkeys(peoples, 0)
count = 0


while True:
    count += 1
    game[current % N] += 1

    if game[current % N] >= M:
        break

    if game[current % N] % 2 != 0:
        current = (current + L) % N
    else:
        current = ((current + N) - L) % N


print(count - 1)
