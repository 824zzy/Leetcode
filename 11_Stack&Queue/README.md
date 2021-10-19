# Note

## Monotonic Stack Template

1. Store index in the monotonic stack can always save space.
2. Monotonic stack sometime can help building a hash table.(496)

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
