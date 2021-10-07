### collections.deque

<br>

- 이중연결리스트로 양 끝단의 삽입과 삭제가 O(1)
- 배열에서 가장 앞의 원소를 삭제하면 배열에 존재하는 원소들을 모두 앞당겨야 하므로 O(n)

```python
from collections import deque

deq = deque()
deq = deque([1, 2, 3])

deq.append(value) # 오른쪽 끝 삽입 O(1)
deq.appendLeft(value) # 왼쪽 끝 삽입 O(1)
deq.pop() # 오른쪽 끝 삭제 O(1)
deq.popLeft() # 왼쪽 끝 삭제 O(1)
deq.remove(value) # value를 찾아서 삭제 O(n)
```
