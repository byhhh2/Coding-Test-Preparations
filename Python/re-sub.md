### 정규 표현식으로 문자열 치환

<br>

```python

import re

text = 'pithon fython'
newText = re.sub('pithon|fython', "python", text)
## python python

```

- `|` 를 사용하면 여러 문자를 한 문자로 바꿀 수 있다.

<br>

```python

import re

print(re.sub('[kj]-pop','good',input()))

# >> k-pop
# good

# >> j-pop
# good

```

- `[]` 로 or을 사용할 수 있다.
