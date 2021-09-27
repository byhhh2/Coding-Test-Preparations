import sys
from collections import Counter

read = sys.stdin.readline().rstrip()
input = read

cntList = Counter(input.upper()).most_common()

if len(cntList) > 1 and cntList[0][1] == cntList[1][1]:
    print('?')
else:
    print(cntList[0][0])
