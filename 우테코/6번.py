# 마지막 호치민 
# 휴가시간 배열 내에서도 나눠써야 할 듯 

def time_cal(input):
    if 'AM' in input:
        if '12AM' in input:
            return 0
        return int(input.replace('AM','')) * 60
    elif 'PM' in input:
        if '12PM' in input:
            return (12 * 60)
        return (12 * 60) + (int(input.replace('PM','')) * 60)

def solution(time, plans):
    answer = ''

    monday_in = 780
    friday_out = 1080
    remain_time = time * 60
    prev = '호치민'

    for p in plans:
        place, go, arrive = p[0], time_cal(p[1]), time_cal(p[2])

        if friday_out - go > 0:
            remain_time -= (friday_out - go)
            if remain_time < 0:
                return prev
        
        if arrive - monday_in > 0:
            remain_time -= arrive - monday_in
            if remain_time < 0:
                return prev

        prev = place

    return answer

