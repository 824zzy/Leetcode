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

## Difference Array (Sweep Line)

Note that for all interval inputs, this method should be the first intuition you come up with.
Essentially it uses a prefix sum counter to calculate overlaps at each index.

### Sweep Line Template 1

``` py
n = len(A)
diff = [0]*(n+1) # 1 indexed array needs one more space.
for i, j in A:
    diff[i] += 1 # or diff[i-1] += 1
    diff[j+1] -= 1 # or diff[j] -= 1

cnt = 0
for i in range(1, n+1): # or for i in range(1, n):
    cnt += diff[i]
    # logic
```

### Sweep Line Template 2

``` py
diff = []
for i, j in A:
    diff.append((i, 1)) # or diff.append((i-1, 1))
    diff.append((j+1, -1)) # or diff.append((j, 1))
diff.sort()

cnt = 0
for _, i in diff:
    cnt += i
    `logic`
```


## Prefix Suffix Decomposition

1. compute suffix array
2. go through prefix and find the answer based on its suffix

## Prefix sum + Hash table

1. count total number of subarrays: 560, 930, 974

```py
cnt = Counter([0])
ans = 0
prefix = 0
for n in A:
    # update prefix
    prefix = prefix+n 
    # update answer
    ans += cnt[prefix-k]
    # update hash table
    cnt[prefix] += 1
return ans
```

2. find longest subarrays: 2106, 523, 525

```py
cnt = {0: -1}
prefix = 0
ans = 0
for i, n in enumerate(A):
    prefix += n
    if prefix-x in cnt: ans = max(ans, i-cnt[prefix-x])
    cnt.setdefault(prefix, i)
return ans
```