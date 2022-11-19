import sys
import re


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b


N = int(sys.stdin.readline())
expression = sys.stdin.readline().strip()
operands = {}
stack = []

for i in range(N):
    operands[chr(i + 65)] = int(sys.stdin.readline())

for elem in expression:
    if bool(re.match('[A-Z]', elem)):
        stack.append(operands[elem])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(calculate(a, b, elem))

print(f'{stack[0]:.2f}')
