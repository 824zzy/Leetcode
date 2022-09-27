# Farmost Smaller Greater Monotonic Stack

## Template

``` py
stk = []
for i in range(len(A)):
    if not stk or A[stk[-1]]>A[i]:
        stk.append(i)

ans = 0
for i in reversed(range(len(A))):
    while stk and A[stk[-1]]<A[i]:
        ans = max(ans, i-stk.pop())
return ans
```
