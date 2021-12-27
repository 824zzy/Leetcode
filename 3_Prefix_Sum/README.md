# Prefix Sum template

- `itertools.accumulate(A)`: prefix sum of A
- `itertools.accumulate(A, mul)`: prefix profuct of A

## Subarray type

```py
cnt = Counter()
cnt[0] = 1
ans = 0
prefix = 0
for n in nums:
    prefix += n # sum type
    ans += cnt[prefix-k] # sum type

    prefix = (prefix + n) % K # division type
    ans += cnt[prefix] # division type

    cnt[prefix] += 1
return ans
```
