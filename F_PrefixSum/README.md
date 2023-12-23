# Prefix Sum template

## Basic operations

1. Compute the 1D prefix sum/product of A

``` py
# prefix sum of A
itertools.accumulate(A)
# prefix product of A
itertools.accumulate(A, mul)
```

2. Compute the 2D prefix sum of A

``` py
# 2D prefix sum of A from top left to bottom right
m, n = len(A), len(A[0])
prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(m):
    for j in range(n): 
        prefix[i+1][j+1] = A[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]

# 2D prefix sum of A from bottom right to top left
m, n = len(A), len(A[0])
prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in reversed(range(1, m+1)):
    for j in reversed(range(1, n+1)): 
        prefix[i-1][j-1] = A[i-1][j-1] + prefix[i][j-1] + prefix[i-1][j] - prefix[i][j]
```
