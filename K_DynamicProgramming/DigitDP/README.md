# Digit DP template

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
