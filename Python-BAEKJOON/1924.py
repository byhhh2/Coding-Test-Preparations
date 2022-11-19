import sys

month, day = map(int, sys.stdin.readline().split())

month31Days = [1, 3, 5, 7, 8, 10, 12]
month30Days = [4, 6, 9, 11]
month28Days = [2]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

numberOfDays = 0

for m in range(1, month):
    if m in month31Days:
        numberOfDays += 31
    elif m in month30Days:
        numberOfDays += 30
    else:
        numberOfDays += 28

numberOfDays += day

print(days[numberOfDays % 7])
