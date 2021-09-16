# 균형잡힌 세상

import sys

_input = ''


def isBalance(string):
    stack = []

    for s in string:
        if (s == '(' or s == '['):
            stack.append(s)
        elif (s == ')' or s == ']'):
            if(len(stack) == 0):
                print('no')
                return
            if (stack[-1] == '(' and s == ')'):
                stack.pop()
            elif (stack[-1] == '[' and s == ']'):
                stack.pop()
            else:
                print('no')
                return

    if (len(stack) == 0):
        print("yes")
    else:
        print("no")



while(1):
    _input = sys.stdin.readline().rstrip()
    if(_input == '.'):
        break
    isBalance(_input)
    
