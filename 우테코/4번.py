def solution(s):
    answer = []

    # start == end
    if s[0] == s[-1]:
        # init
        cur = s[0]
        start = 0
        end = len(s) - 1
        cnt = 2

        while True:
            start += 1
            if len(s) - 1 > start and s[start] == cur:
                cnt += 1
            else:
                break

        if start < len(s) - 1:
            while True:
                end -= 1
                if len(s) - 1 > end and s[end] == cur:
                    cnt += 1
                else:
                    break

        answer.append(cnt)

        # print(start, end)
        

        # remain
        cur = s[start]
        cnt = 1

        for i in range(start, end):
            if cur == s[i + 1]:
                cnt += 1
                if i + 1 == end:
                    answer.append(cnt)
                    cnt = 1
            else:
                cur = s[i + 1]
                answer.append(cnt)
                cnt = 1
                if i + 1 == end:
                    answer.append(1)
    else:
        cur = s[0]
        cnt = 1
        for i in range(0, len(s) - 1):
            if cur == s[i + 1]:
                cnt += 1
                if i + 1 == len(s) - 1:
                    answer.append(cnt)
                    cnt = 1
            else:
                cur = s[i + 1]
                answer.append(cnt)
                cnt = 1
                if i + 1 == len(s) - 1:
                    answer.append(1)

    return sorted(answer)

# print(solution("aaabbaaa"))
# print(solution("wowwow"))
print(solution("aaba"))