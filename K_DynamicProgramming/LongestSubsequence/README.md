# Longest Increasing Subsequence

## Type 1: Longest Increasing Subsequence

Bottom up template:

``` py
dp = [1] * len(A)
for i in range(1, len(A)):
    for j in range(i):
        if A[j]<A[i]:
            dp[i] = max(dp[i], dp[j]+ 1)
return max(dp)
```

Top down template:

``` py
@cache
def dp(i):
    ans = 1
    for j in range(i):
        if A[j]<A[i]:
            ans = max(ans, 1+dp(j))
    return ans

return max(dp(i) for i in range(len(A)))
```

## Type 2: Longest Common Subsequence

Consider using hash table or binary search to optimize the time complexity.
