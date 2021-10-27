import sys

dic = {}

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if str(a) + ',' + str(b) + ',' + str(c) in dic:
        return dic[str(a) + ',' + str(b) + ',' + str(c)]

    if a < b < c:
        dic[str(a) + ',' + str(b) + ',' + str(c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dic[str(a) + ',' + str(b) + ',' + str(c)]
    else:
        dic[str(a) + ',' + str(b) + ',' + str(c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dic[str(a) + ',' + str(b) + ',' + str(c)]


while True:
    A, B, C = map(int, sys.stdin.readline().split())
    saveA = A
    saveB = B
    saveC = C

    if A == -1 and B == -1 and C == -1:
        break

    print(f'w({saveA}, {saveB}, {saveC}) = {w(A, B, C)}')
