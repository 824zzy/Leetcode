""" https://leetcode.com/problems/counting-bits/
bit manipulation+dp
Set i's lowest 1 to 0 by `i&(i-1)`, then dp(i)==dp(i&(i-1))+1
"""
# top down
class Solution:
    def countBits(self, n: int) -> List[int]:
        @cache
        def dp(i):
            if i==0: return 0
            return dp(i&(i-1))+1
            
        return [dp(i) for i in range(n+1)]

# bottom up
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(1, n+1):
            ans[i] = ans[i&(i-1)]+1
        return ans
            