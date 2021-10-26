import sys

one_arr = []
zero_arr = []

def oneCounter(N):
    try:
        return one_arr[N]
    except IndexError:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return oneCounter(N-1) + oneCounter(N-2)

def zeroCounter(N):
    try:
        return zero_arr[N]
    except IndexError:
        if N == 0:
            return 1
        elif N == 1:
            return 0
        else:
            return zeroCounter(N-1) + zeroCounter(N-2)

def addOneArr(N):
    global one_arr

    for i in range(0, N + 1):
        one_arr.append(oneCounter(i))

    return one_arr[N]
    

def addZeroArr(N):
    global zero_arr

    for i in range(0, N + 1):
        zero_arr.append(zeroCounter(i))

    return zero_arr[N]
    

T = int(sys.stdin.readline())

for i in range(T):
    one_arr = []
    zero_arr = []
    N = int(sys.stdin.readline())

    print(addZeroArr(N), addOneArr(N))