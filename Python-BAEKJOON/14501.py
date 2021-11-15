import sys

N = int(sys.stdin.readline())
schedule = [[]]

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())
    schedule.append([T, P])

max_money = 0

def isAble(day, cost):
    global max_money

    if day <= N:
        if day + schedule[day][0] <= N + 1:
            isAble(day + schedule[day][0], cost + schedule[day][1])
        isAble(day + 1, cost)
    else:
        if cost > max_money: 
            max_money = cost

for day in range(1, N + 1): 
    if day + schedule[day][0] <= N + 1:
        isAble(day + schedule[day][0], schedule[day][1])

print(max_money)