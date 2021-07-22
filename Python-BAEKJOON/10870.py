# 피보나치

n1 = 0
n2 = 1
result = 0

n = int(input())

if (n == n1 or n == n2):
    print(n)
    quit()


for i in range(1, n):
    result = n1 + n2
    n1 = n2
    n2 = result

print(result)