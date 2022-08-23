# Sweep Line

Note that for all interval inputs, this method should be the first intuition you come up with.
Essentially it uses a prefix sum counter to calculate overlaps at each index.

## Sweep Line Template 1

``` py
SL = []
for i, j in A:
    SL.extend([[i, 1], [j, -1]])
SL.sort()

cnt = 0
for _, i in SL:
    cnt += i
    `logic`
```

## Sweep Line Template 2

``` py
n = len(A)
SL = [0]*(n+1) # 1 indexed array needs one more space.
for i, j in A:
    SL[i] += 1 # or SL[i-1] += 1
    SL[j+1] -= 1 # or SL[j] -= 1

cnt = 0
for i in range(1, n+1): # or for i in range(1, n):
    cnt += SL[i]
    # logic
```
