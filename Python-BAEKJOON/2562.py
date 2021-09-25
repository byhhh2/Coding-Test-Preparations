import sys

max = 0
maxIndex = 0

for i in range(9):
    input = int(sys.stdin.readline()) 
    if max < input:
        max = input
        maxIndex = i + 1

print(max)
print(maxIndex)