# Note

## Monotonic Stack Template

Store index in the monotonic stack can always save space.

``` py
s = []
for i in range(len(A)):
    while s and `condition`:
        `logic`
        s.pop()
    if `condition`:
        s.append(A[i]) / s.append(i)
return ans
```
