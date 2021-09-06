# 수들의 합

S = int(input())

sumPrediction = 0
i = 1

while(1):
    if ((i * (i + 1)) / 2 <= S and S < ((i + 1) * (i + 2)) / 2):
        sumPrediction = i
        break
    i += 1

print(i)
