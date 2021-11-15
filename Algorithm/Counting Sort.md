### 계수 정렬, Counting Sort

<br>

- 문제 <a href="https://www.acmicpc.net/problem/10989">수 정렬하기 3</a>
  - 메모리 제한은 8MB
  - 수가 `10,000,000`개 들어온다면 `int`가 `4byte = 40MB`이므로 **메모리초과**
  - 즉, 들어오는 수를 배열에 모두 저장해서 `sort`하는 방식은 불가능하다.

<br>

### 특징

- `O(n)`이라는 시간
- 정렬할 숫자가 특정 범위안에 있을 때 사용 (예: 알파벳)
- 시간을 줄이기위해 누적합을 사용할 수 있다. (아래의 링크 참조)

<br>

### 코드

```python
import sys

N = int(sys.stdin.readline())
input = []

counter = [0] * 10001

for i in range(N):
   counter[int(sys.stdin.readline())] += 1

for i in range(0, 10001):
    if counter[i] != 0: # 여기서 0이 많으면 낭비일때 누적합사용
        for j in range(counter[i]):
            print(i)
```

<br>

### 시간 복잡도

- `O(n)`
- 엄청난 메모리 낭비를 야기

<br>

### 참고

- <a href="https://bowbowbow.tistory.com/8">Counting Sort + 누적합</a>
