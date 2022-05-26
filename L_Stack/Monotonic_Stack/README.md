# Monotonic Stack

The monotonic increasing stack and monotonic decreasing stack, namely monotonic stack, is a very powerful tool for finding next greater/smaller element.
More specifically, always **use monotonic increasing stack when we are trying to find the next smaller element, vice versa.**
And in the template, `A[stk[-1]]>A[i]` indiates a monotonic increasing stack.

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
