# 최대공약수와 최소공배수 

def gof(a, b):
    while(b != 0):
        result = a % b
        a = b
        b = result
    print(a)

def lcf(a, b):
    i = 1
    while(True):
        a *= i
        if (a % b == 0):
            print(a)
            break
        a //= i
        i += 1

values = input().split()

if (values[0] > values[1]):
    a = int(values[0])
    b = int(values[1])
else:
    b = int(values[0])
    a = int(values[1])

gof(a, b)
lcf(a, b)