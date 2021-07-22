# 백설공주와 난쟁이들, 난쟁이들의 키 합은 100 

totalHeight = 0
heightArray = []
targetNum = 0
flag = 0

for i in range(0, 9):
    height = int(input())
    heightArray.append(height)
    totalHeight += height

targetNum = totalHeight - 100

for i in range(0, 9):
    for j in range(i + 1, 9):
        if(heightArray[i] + heightArray[j] == targetNum):
            tmp_i = heightArray[i]
            tmp_j = heightArray[j]
            heightArray.remove(tmp_i)
            heightArray.remove(tmp_j)
            flag = 1
            break
    if(flag == 1):
        break

heightArray.sort()

for h in heightArray:
    print(h)