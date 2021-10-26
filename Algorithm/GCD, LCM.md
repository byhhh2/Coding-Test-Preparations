## GCD, LCM | 유클리드 호제법

<br>

### GCD, Greatest Common Divisor, 최대공약수

```python
def GCD(A, B):
    while True:
        C = A % B
        if C == 0:
            return B
        A = B
        B = C
```

<br>

```
GCD(A, B) = GCD(A, A % B)
if A % B = 0 -> GCD = B
```

<br>
<br>

### LCM, Least Common Multiple, 최소공배수

```python
def LCM(A, B, gcd):
    return (A * B) // gcd
```

<br>

```
LCM = (A * B) / GCD
```

<br>
<br>

- <a href="https://myjamong.tistory.com/138">참고한 블로그</a>
