N = int(input())
values = input().split()

for i in range(0, N):
    value = int(values[i])
    if (i == 0):
        max = value
        min = value
    else:
        if(value < min):
            min = value
        if(value > max):
            max = value
print(min , max)
