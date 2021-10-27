- 한번 계산한 결과를 메모리에 저장하여 중복 계산을 방지
- DP의 핵심 기술

<br>

## 피보나치 수열

- 피보나치 수열에서 f(5)를 구하기 위한 계산은 f(3)이 2번, f(2)가 3번, f(1)이 5번으로 중복 계산되는 값이 많다. 이 경우 시간복잡도가 크다.

<br>

## 메모이제이션 활용

- <a href="https://www.acmicpc.net/problem/9184">예시문제 : 백준 9184, 신나는 함수 실행</a>

```
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
```

- 위와 같은 재귀함수가 존재하며 재귀를 통해 w함수를 구현할 경우 a, b, c값이 어느정도 크면 오랜 시간이 걸린다.

<br>

### 메모이제이션을 활용한 풀이

```python
import sys

dic = {}

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if str(a) + ',' + str(b) + ',' + str(c) in dic:
        return dic[str(a) + ',' + str(b) + ',' + str(c)]
    ## dictionary에 이미 존재하는 값이라면 그 값을 return해서 시간을 줄인다.

    if a < b < c:
        dic[str(a) + ',' + str(b) + ',' + str(c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dic[str(a) + ',' + str(b) + ',' + str(c)]
    else:
        dic[str(a) + ',' + str(b) + ',' + str(c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dic[str(a) + ',' + str(b) + ',' + str(c)]


while True:
    A, B, C = map(int, sys.stdin.readline().split())
    saveA = A
    saveB = B
    saveC = C

    if A == -1 and B == -1 and C == -1:
        break

    print(f'w({saveA}, {saveB}, {saveC}) = {w(A, B, C)}')

```

<br>
<br>

- <a href="https://namu.wiki/w/%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98?__cf_chl_managed_tk__=pmd_Cc_bY2SjH004ePb6qCiCrLhVw86urQrTgc3EkA2mAog-1635324401-0-gqNtZGzNA2WjcnBszQkl">참고 - 나무위키 : 메모이제이션</a>
