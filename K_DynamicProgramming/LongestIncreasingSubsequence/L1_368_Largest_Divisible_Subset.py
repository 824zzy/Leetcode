""" https://leetcode.com/problems/largest-divisible-subset/
Sort A in ascending order. 
dp[i] means contains the largest subset containing A[i].

# Time complexity: O(N^2)
"""
from header import *

# bottom up
class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        A.sort()
        dp = [[A[i]] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                if A[i]%A[j]==0:
                    dp[i] = max(dp[i], dp[j]+[A[i]], key=len)
        return max(dp, key=len)


# top down solution which is easy to understand but not efficient
class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        A.sort()
        
        @cache
        def dp(i):
            ans = [A[i]]
            for j in range(i):
                if A[i]%A[j]==0:
                    ans = max(ans, dp(j)+[A[i]], key=len)
            return ans
            
        return max([dp(i) for i in range(len(A))], key=len)