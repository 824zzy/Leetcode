# Note

## Monotonic Stack Template

``` py
s = []
for i in range(len(A)):
    while s and `condition`:
        `logic`
        s.pop()
    if `condition`:
        s.append(A[i])
return ans
```
