def solution(grid, clockwise):
    answer = []

    for i, j in zip(range(len(grid) - 1, -1, -1), list(range(0, len(grid)))):
        grid[j] = ('-' * i) + grid[j] + ('-' * i)

    print(grid)

    if clockwise:
        cur_x = len(grid)-1
        cur_y = 0

        answer.append(grid[cur_x][cur_y])

        # len(grid) - 1 가운데 열 
        # while cur_y <= len(grid) - 1:
        for i in range(1, len(grid)):
            cur_y += 1 
            cur_x -= 1

            flag = 0
            add_x = cur_x
            add_y = cur_x
            add_string = ''
            # 한 줄 

            for j in range(1 + (i * 2)):
                add_string += grid[add_x][add_y]

                print(cur_x, cur_y, )

                if flag == 0:
                    add_x += 1
                    flag = 1
                else:
                    add_y += 1
                    flag = 0

            answer.append(add_string)

    print(answer)
                
    return answer


solution(["1","234","56789"], True)