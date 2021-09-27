# import sys

# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# cnt = 0

# input = sys.stdin.readline().rstrip()

# for c in croatia:
#     if c in input:
#         cnt += input.count(c)
#         input = input.replace(c, '0')

# input = input.replace('0', '')
# cnt += len(input)
# print(cnt)

import re

print(len(re.sub('c=|c-|dz=|d-|lj|nj|s=|z=','Z',input())))