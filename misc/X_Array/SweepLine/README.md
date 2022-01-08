# Sweep Line template

Note that for all intervals inputs, this method should be the first intuition you come up with.
Essentially it uses a prefix sum counter to calculate overlaps at each index.

``` py
n = len(A)
cnt = [0] * (n + 1) # 1 indexed array needs one more space.
for i, j in req:
    cnt[i] += 1 # or cnt[i-1] += 1
    cnt[j+1] -= 1 # or cnt[j] -= 1
for i in range(1, n+1): # or for i in range(1, n):
    cnt[i] += cnt[i - 1]
```
