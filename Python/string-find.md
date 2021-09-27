- `find()` 의 경우 값이 없을 경우 -1를 리턴하지만, `index()`는 error

<br>

```python

text = '가나다라마바사`

text.find('나다') # 1
text.find('아자차') # -1

```
