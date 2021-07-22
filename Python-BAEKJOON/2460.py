# 지능형 기차

maxNum = 0
totalNum = 0

for i in range(1, 11):
    values = input().split()
    totalNum = totalNum-int(values[0])+int(values[1])
    if (maxNum < totalNum):
        maxNum = totalNum
    
print(maxNum)