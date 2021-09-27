import sys

input = sys.stdin.readline().rstrip()

sum = 0
list = [('ABC', 3), ('DEF', 4), ('GHI', 5), ('JKL', 6), 
        ('MNO', 7), ('PQRS', 8), ('TUV', 9), ('WXYZ', 10)]

def returnTime(ch):
    for l in list:
        if ch in l[0]:
            return l[1]

for i in input:
    sum += returnTime(i)

print(sum)