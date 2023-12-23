## Prefix sum + Hash table

1. count total number of subarrays: 560, 930, 974

```py
seen = Counter([0])
ans = 0
prefix = 0
for n in A:
    # update prefix
    prefix = prefix+n 
    # update answer
    ans += seen[prefix-k]
    # update hash table
    seen[prefix] += 1
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