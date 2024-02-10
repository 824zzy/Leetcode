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
    

# knap sack solution
"""
knap sack:
1. sort the array to ensure&check whether the larger element can divide the previous element
2. for each element, we have two choice:
    1. skip it
    2. choose it if the current element can divide previous one
"""
class Solution:
    def largestDivisibleSubset(self, A: List[int]) -> List[int]:
        A.sort()
        
        @cache
        def dp(i, pre):
            if i==len(A):
                return []
            # skip
            ans = dp(i+1, pre)
            # choose
            if pre==None or A[i]%pre==0:
                ans = max(ans, [A[i]]+dp(i+1, A[i]), key=len)
            return ans
        return dp(0, None)