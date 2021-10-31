# Sweep Line template

Note that for all intervals inputs, this method should be the first intuition you come up with.
Essentially it uses a prefix sum counter to calculate overlaps at each index.

``` py
n = len(A)
count = [0] * (n + 1) # 1 indexed array needs one more space.
for i, j in req:
    count[i] += 1 # or count[i-1] += 1
    count[j+1] -= 1 # or count[j] -= 1
for i in range(1, n+1): # or for i in range(1, n):
    count[i] += count[i - 1]
```
