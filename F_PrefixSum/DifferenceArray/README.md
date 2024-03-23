# Difference Array (Sweep Line)

Note that for all interval inputs, this method should be the first intuition you come up with.
Essentially it uses a prefix sum counter to calculate overlaps at each index.

## Sweep Line Template 1

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

## Sweep Line Template 2

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
