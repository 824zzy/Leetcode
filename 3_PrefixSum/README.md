# Prefix Sum template

- `itertools.accumulate(A)`: prefix sum of A
- `itertools.accumulate(A, mul)`: prefix profuct of A

## Basic type

## Subarray type

1. count total number of subarrays: 560, 930, 974

```py
cnt = Counter([0])
ans = 0
prefix = 0
for n in A:
    prefix = prefix+n # or modulo (prefix + n) % K
    ans += cnt[prefix-k] # or modulo cnt[prefix]
    cnt[prefix] += 1
return ans
```

2. find longest subarrays: 2106, 523, 525

```py
seen = {0: -1}
prefix = 0
ans = 0
for i, n in enumerate(A):
    prefix += n
    if prefix-x in seen: ans = max(ans, i-seen[prefix-x])
    seen.setdefault(prefix, i)
return ans
```
