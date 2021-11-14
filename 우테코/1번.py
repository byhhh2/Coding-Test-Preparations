from collections import Counter

def solution(arr):
    answer = []
    max = 0
    dict_counter = dict(Counter(arr))


    if len(dict_counter) == 1:
        l = len(arr)
        a = arr[0]
        return_list = []

        for i in range(3):
            if i == a - 1:
                return_list.append(0)
            else:
                return_list.append(l)


        return return_list

    elif len(dict_counter) == 2:
        return_list = []
        not_in = 0

        for item in dict_counter:
            if max < dict_counter[item]:
                max = dict_counter[item]
        
        for i in range(1, 4):
            if i not in dict_counter:
                not_in = i

        for i in range(1, 4):
            if i == not_in:
                return_list.append(max)
            else:
                return_list.append(max - dict_counter[i])

        return return_list 


    for item in dict_counter:
        if max < dict_counter[item]:
            max = dict_counter[item]

    for i in sorted(dict_counter.items()):
        answer.append(max - i[1])

    return answer


solution([2,1,3,1,2,1])

