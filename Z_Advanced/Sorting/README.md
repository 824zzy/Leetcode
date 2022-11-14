# Sorting Algorithms

## Cycle Sort

``` py
def cyclesort(A):
    mp = {x: i for i, x in enumerate(sorted(A))}
    seen = {x: False for x in A}
    ans = 0
    for i, x in enumerate(A):
        cnt = 0
        while i!=mp[x] and not seen[x]:
            cnt += 1
            seen[x] = True
            i = mp[x]
            x = A[i]
        ans += max(0, cnt-1)
    return ans   
```

## Reference

1. [Cycle Sort](https://www.geeksforgeeks.org/cycle-sort/)
