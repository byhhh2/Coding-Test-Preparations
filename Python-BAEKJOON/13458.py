import sys

N = int(sys.stdin.readline())

A = sys.stdin.readline()
AList = list(map(int, A.split()))

B, C = map(int, sys.stdin.readline().split())

totalViewer = 0

for A in AList:
    students = A
    students -= B
    totalViewer += 1
    if students > 0:
        totalViewer += students // C
        if students % C != 0:
            totalViewer += 1
    
print(totalViewer)