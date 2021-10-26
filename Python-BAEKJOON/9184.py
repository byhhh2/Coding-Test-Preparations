import sys

dic = {}

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if str(a) + ',' + str(b) + ',' + str(c) in dic:
        return dic[str(a) + ',' + str(b) + ',' + str(c)]

    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


def addArr(a, b, c):
    global arr 
    global dic
    arr = []
    dic = {}

    for i in range(0, a + 1):
        for j in range(0, b + 1):
            for k in range(0, c + 1):
                dic[str(i) + ',' + str(j) + ',' + str(k)] = w(i, j, k)


while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == -1 and B == -1 and C == -1:
        break
    elif A > 20 or B > 20 or C > 20:
        A, B, C = 20, 20, 20
    elif A <= 0 or B <= 0 or C <= 0:
        print(1)
        continue

    addArr(A, B, C)
    S = dic[str(A) + ',' + str(B) + ',' + str(C)]

    print(f'w({A}, {B}, {C}) = {S}')
 

