""" https://leetcode.com/problems/longest-increasing-subsequence/
one of the most famous leetcode problem, 

1. use bisect to maintain a increasing list. O(NlogN)
2. use dp[i] denotes length of the longest subsequence from begining & ending at ith element. O(N^2)

"""
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        vals = []
        for x in A: 
            k = bisect_left(vals, x)
            if k == len(vals): vals.append(x)
            else: vals[k] = x
        return len(vals)


# top down dp
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i==len(A): return 0
            ans = 1
            for j in range(i):
                if A[j]<A[i]:
                    ans = max(ans, 1+dp(j))
            return ans
        
        return max(dp(i) for i in range(len(A)))

# bottom up dp
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = [1] * len(A)
        for i in range(1, len(A)):
            for j in range(i):
                if A[j]<A[i]:
                    dp[i] = max(dp[i], dp[j]+ 1)
        return max(dp)