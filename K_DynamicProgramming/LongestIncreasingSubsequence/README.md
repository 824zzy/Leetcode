# Longest Increasing Subsequence (LIS)

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
In O(n^2) time complexity, the dp[i] represents **the length** of the longest increasing subsequence **ending at index i**.
In order to improve the time complexity to O(nlogn), we need to think reversely: dp[i] represents **the minimum value** of the last element of the increasing subsequence with **length i+1**. The reason is that we can update the dp array with binary search.

TODO: add 3288


``` python
# O(N^2) dp
def LIS(A):
    dp = [1] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# O(NlogN) binary search + greedy
def LIS(A):
    dp = []
    for x in A:
        k = bisect_left(dp, x)
        if k == len(dp):
            dp.append(x)
        else:
            dp[k] = x
    return len(dp)
```