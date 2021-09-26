def isSelfNum(num):
    n = num - 1

    while n > 0:
        tmp = n 
        digitList = []

        while tmp != 0:
            digitList.append(tmp % 10)
            tmp //= 10

        if n + sum(digitList) == num:
            return False
        n -= 1
    return True


for i in range(1, 10001):
    if isSelfNum(i) == True:
        print(i)