
# n == 1 : 1
# n == 2 : 11, 00
# n == 3 : 001, 100, 111
# n == 4 : 0011, 0000, 1001, 1100, 1111
# n == 5 : 00001, 10000, 00111, 11100, 10011, 11001, 00100, 11111


# import sys

# def count(n):
#     arr = [['1'], ['00', '11']]

#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         base = 2

#         while base < n:
#             cur = set()

#             for a in arr[base - 2]:
#                 cur.add(a + '00')
#                 cur.add('00' + a)
#             for a in arr[base - 1]:
#                 cur.add(a + '1')
#                 cur.add('1' + a)

#             arr.append(list(cur))
#             base += 1

#     print(arr[-1])
    
#     return len(arr[-1])      
      

# input = int(sys.stdin.readline())
# print(count(input) % 15746)

import sys

countList = [0, 1, 2]

def countTile(n):
    for i in range(3, n + 1):
        countList.append((countList[i - 2] + countList[i - 1]) % 15746)

    print(countList[n])

N = int(sys.stdin.readline())

countTile(N)