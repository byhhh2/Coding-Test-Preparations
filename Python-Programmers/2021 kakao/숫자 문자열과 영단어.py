def solution(s):
    answer = 0
    
    numList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(0, 10):
        if numList[i] in s:
            s = s.replace(numList[i], str(i))
    
    answer = int(s)
    
    return answer