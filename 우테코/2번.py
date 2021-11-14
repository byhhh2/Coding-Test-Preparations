def solution(log):
    answer = ''
    time_limit = 105
    total_time = 0

    for i in range(0, len(log), 2):
        start_h = int(log[i][0:2])
        start_m = int(log[i][3:5])
        start = (start_h * 60) + start_m

        end_h = int(log[i + 1][0:2])
        end_m = int(log[i + 1][3:5])
        end = (end_h * 60) + end_m

        if end - start > time_limit:
            total_time += time_limit
            continue
        elif end - start < 5:
            continue
        total_time += end - start

    total_h = total_time // 60
    total_m = total_time % 60

    answer = '{0:02}:{1:02}'.format(total_h, total_m)

    return answer

print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))