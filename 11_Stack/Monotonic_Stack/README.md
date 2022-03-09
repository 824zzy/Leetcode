# Monotonic Stack Template

1. Store index in the monotonic stack can always save space.
2. Monotonic stack sometime can help building a hash table.(496)

## Template

``` py
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]]?A[i]:
        `logic`
        stk.pop()
    `logic`
    stk.append([i, A[i]])
return ans
```
