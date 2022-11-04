# Monotonic Stack

The monotonic increasing stack and monotonic decreasing stack, namely monotonic stack, is a very powerful tool for finding next greater/smaller element.
More specifically, always **use monotonic increasing stack when we are trying to find the next smallerer element, vice versa.**
And in the template, `A[stk[-1]]>A[i]` indicates a monotonic increasing stack.

## Template

Basic template:

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

Two pass to find next smaller elements:

``` py
# next smaller on the right
R = [len(A)]*len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]]>A[i]:
        R[stk.pop()] = i
    stk.append(i)

# next smaller on the left
L = [-1]*len(A)
stk = []
for i in reversed(range(len(A))):
    while stk and A[stk[-1]]>=A[i]:
        L[stk.pop()] = i
    stk.append(i)
```

Two pass to find next greater elements:

``` py
# next greater on the right
R = [len(A)]*len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]]<A[i]:
        R[stk.pop()] = i
    stk.append(i)

# next greater on the left
L = [-1]*len(A)
stk = []
for i in reversed(range(len(A))):
    while stk and A[stk[-1]]<A[i]:
        L[stk.pop()] = i
    stk.append(i)
```
