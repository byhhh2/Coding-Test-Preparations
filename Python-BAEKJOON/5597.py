import sys

totalStudent = [_ for _ in range(1, 31)]
submitted = []
notSubmitted = []

for i in range(28):
    submitted.append(int(sys.stdin.readline()))


for student in totalStudent:
    if student not in submitted:
        notSubmitted.append(student)

for student in sorted(notSubmitted):
    print(student)
