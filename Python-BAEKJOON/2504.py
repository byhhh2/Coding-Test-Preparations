# 괄호열 출력

_input = input()
stack = []
result = 1
result_string = ''

if (_input[0] == ')' or _input[0] == ']'):
    print(0)
    quit()

for item in _input:
    if (item == '(' or item == '['):
        stack.append(item)
    elif (len(stack) == 0):
        print(0)
        quit()
    else:
        if ((stack[-1] == '(' and item == ')') or (stack[-1] == '[' and item == ']')):
            stack.pop()


if (len(stack) != 0):
    print(0)
else:
    _input = _input.replace(')(', ')+(')
    _input = _input.replace(')[', ')+[')
    _input = _input.replace('](', ']+(')
    _input = _input.replace('][', ']+[')

    # print(_input)

    for i in _input:
        if (i == '('):
            result_string = result_string + '2 * ('
        elif (i == '['):
            result_string = result_string + '3 * ('
        elif (i == ')' or i == ']'):
            result_string = result_string + ')'
        elif (i == '+'):
            result_string = result_string + '+'

    result_string = result_string.replace('()', '1')
    print(eval(result_string))
