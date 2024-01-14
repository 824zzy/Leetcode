# Digits DP template

## Digits DP basic template
``` py
high = str(n)
n = len(high)
@cache
def dfs(i, limit):
    if i==n:
        # update answer count
        return 1
    ans = 0
    hi = int(high[i]) if limit else 9
    for d in range(hi+1):
        ans += dfs(i+1, limit and d==int(high[i]))
    return ans
```

## Digits DP template supports lower and upper bound
``` py
high = str(n)
n = len(high)
low = str(0).zfill(n)

@cache
def dfs(i, limit_low, limit_high):
    if i==n:
        # update answer count
        return 1
    ans = 0
    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9
    for d in range(lo, hi+1):
        ans += dfs(i+1, limit_low and d==lo, limit_high and d==hi)
    return ans
# add extra parameters if needed
return dfs(0, True, True)
```

## Digits DP template supports leading zero (Most Popular)
``` py
high = str(n)
n = len(high)
low = str(0).zfill(n)

@cache
def dfs(i, limit_low, limit_high, is_num):
    if i==n:
        # update answer count
        return 1
    ans = 0
    if not is_num and low[i]=='0':
        ans += dfs(i+1, True, False, False)

    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9
    
    d0 = 0 if is_num else 1
    for d in range(max(lo, d0), hi+1):
        ans += dfs(i+1, limit_low and d==lo, limit_high and d==hi, True)
    return ans
```

## Deprecated old template

``` py
"""
i: the current index of the digit array
isPrefix: if the new number is the prefix of N
isBigger: if the new number will be bigger than N when we reach final position

Extra parameters need to be added to the dp function depends on the problem
"""
# upper bound of the digit array
A = list(map(int, str(n)))

@cache
def dp(i, isPrefix, isBigger, *args):
    if i==len(A): return 0
    ans = 0
    for d in range(i==0, 10):
        _isPrefix = isPrefix and d==A[i]
        _isBigger = isBigger or (isPrefix and d>A[i])
        if CONDITION and not(i==len(A)-1 and _isBigger):
            # update answer
        ans += dp(i+1, _isPrefix, _isBigger, *args)
    return ans

return dp(0, True, False)
```

## References

- [migfulcrum](https://leetcode.com/problems/rotated-digits/discuss/560601/python-digit-dp)
- [0x3ff template](https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci/)