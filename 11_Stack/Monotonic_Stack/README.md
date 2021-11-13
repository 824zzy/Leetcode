# Monotonic Stack Template

1. Store index in the monotonic stack can always save space.
2. Monotonic stack sometime can help building a hash table.(496)

## Store index type

``` py
stk = []
ans = A
for i in range(len(A)):
    while stk and A[stk[-1]]>=A[i]:
        `logic`
        stk.pop()
    `logic`
    stk.append(i)
return ans
```

## Store value type

``` py
stk = []
for i in range(len(A)):
    while stk and `condition`:
        `logic`
        stk.pop()
    stk.append(A[i])
return ans
```
