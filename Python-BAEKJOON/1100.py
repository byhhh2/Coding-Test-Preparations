import sys

cnt = 0

for i in range(8):
    input = sys.stdin.readline().rstrip()

    if i % 2 == 0:
        for j in range(0, 8, 2):
            if input[j] == 'F':
                cnt += 1
    else:
        for j in range(1, 8, 2):
            if input[j] == 'F':
                cnt += 1

print(cnt)
