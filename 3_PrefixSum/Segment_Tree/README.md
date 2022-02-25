# Binary Indexed Tree Template

``` py
c = [0] * (max(A)+1)
def update(x):
    while (x <= m):
        c[x] += 1
        x += x & -x

def get(x):
    res = 0
    while (x > 0):
        res += c[x]
        x -= x & -x
    return res

for i, a in enumerate(A):
    res += min(get(a - 1), i - get(a))
    update(a)
```
