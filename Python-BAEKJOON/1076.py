import sys

color = []
table = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

answer = ''

for i in range(3):
    color.append(sys.stdin.readline().rstrip())
    if i == 2:
        print(int(answer) * (10 ** table.index(color[i])))
    answer += str(table.index(color[i]))