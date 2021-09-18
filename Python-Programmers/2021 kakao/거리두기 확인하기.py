def solution(places):
    
    flag = 0
    answer = []
    
    for i in range(0, 5): # 대기실 
        flag = 0
        for j in range(0, 5): # 행
            if flag == 1:
                break
            for k in range(0, 5): # 열
                if flag == 1:
                    break
                if places[i][j][k] == "P":  
                    for l in range(0, 3):
                        for m in range(0, 3 - l):
                            if flag == 1:
                                break
                            if (l == 0 and m == 0):
                                continue
                            if (j + l < 5 and k + m < 5 and places[i][j + l][k + m] == "P"):
                                if (l + m == 1):
                                    flag = 1
                                elif (l == 2):
                                    if places[i][j + 1][k] != "X":
                                        flag = 1
                                elif (m == 2):
                                    if places[i][j][k + 1] != "X":
                                        flag = 1
                                elif (l + m == 2):
                                    if places[i][j + 1][k] != "X" or places[i][j][k + 1] != "X" :
                                        flag = 1 
                        if flag == 1:
                            break
                    
                    if j + 1 < 5 and k - 1 >= 0 and places[i][j + 1][k - 1] == "P":
                        if places[i][j + 1][k] != "X" or places[i][j][k - 1] != "X" : 
                            print(i, j, k)
                            flag = 1


        if flag == 1:
            answer.append(0)
        else:
            answer.append(1)
                                   
    return answer


p =	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(p))