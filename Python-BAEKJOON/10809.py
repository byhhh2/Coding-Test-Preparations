import sys

list = [-1] * 26

input = sys.stdin.readline().rstrip()

for i in input:
    if input.find(i) == -1:
        continue
    else:
        list[ord(i) - 97] = input.find(i)


for l in list:
    print(l, end=' ')
