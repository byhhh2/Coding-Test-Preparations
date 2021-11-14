def solution(rows, columns):
    answer = [[0] * columns for _ in range(rows)]

    answer[0][0] = 1
    r, c = 0, 0
    cur = 1

    while True:
        if rows == columns:
            if answer[rows-1][0] != 0:
                break

        flag = 0

        for a in answer:
            if 0 in a:
                flag = 1
                break

        if flag == 0:
            break

        if cur % 2 == 0:
            r = (r + 1) % rows
        else:
            c = (c + 1) % columns

        cur += 1
        answer[r][c] = cur
    
    return answer


print(solution(6, 6))

