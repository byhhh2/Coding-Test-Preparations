# 동호의 쉬운 문제

A, B = map(int, input().split())
sequence = []
total = 0

for i in range(1, B+1):
    for j in range(i):
        sequence.append(i)

for i in range(A, B+1):
    total += sequence[i - 1]

print(total)
