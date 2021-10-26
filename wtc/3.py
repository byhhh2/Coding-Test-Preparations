import sys

def solution(word):
    answer = ''

    for w in word:
        if ord(w) >= ord('a') and ord(w) <= ord('z'):
            answer += chr(ord('z') - (ord(w) - ord('a')))
        elif ord(w) >= ord('A') and ord(w) <= ord('Z'):
            answer += chr(ord('Z') - (ord(w) - ord('A')))
        else:
            answer += w
        
    return answer


input = sys.stdin.readline()
print(solution(input))