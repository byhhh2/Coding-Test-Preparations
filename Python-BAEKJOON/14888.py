# # N = int(input())
# # A = list(map(int, input().split()))
# # operator_num = list(map(int, input().split()))
# # operator = ['+', '-', '*', '//']
# # using_operator = []

# print(eval('1+2+3-4*5//6'))

# # for k in range(0, 4):
# #     for i in range(0, operator_num[k]):
# #         using_operator.append(operator[k])


# print(op['+'])
# print(op[0])

# 연산자 끼워넣기
# 몰라서 참고함.. 나중에 다시 공부

def DFS(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        DFS(cnt + 1, result + sequence[cnt], p - 1, m, mul, div)
    if m:
        DFS(cnt + 1, result - sequence[cnt], p, m - 1, mul, div)
    if mul:
        DFS(cnt + 1, result * sequence[cnt], p, m, mul - 1, div)
    if div:
        DFS(cnt + 1, -(-result // sequence[cnt]) if result <
            0 else result // sequence[cnt], p, m, mul, div - 1)


n = int(input())
sequence = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_result = -1000000001
min_result = 1000000001

DFS(1, sequence[0], operator[0], operator[1], operator[2], operator[3])

print(max_result)
print(min_result)
