""" L1: https://leetcode.com/problems/ugly-number-ii/
iteratively return next ugly number given an ungly number x
"""
# top down
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        @cache
        def fn(k):
            """Return the smallest ugly number larger than k (not necessarily ugly)."""
            if k == 0: return 1
            return min(f*fn(k//f) for f in (2, 3, 5))
    
        ans = 1
        for _ in range(n-1): ans = fn(ans)
        return ans
   
# bottom up 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        f2, f3, f5 = 0, 0, 0
        for _ in range(n-1):
            x = min(2*dp[f2], 3*dp[f3], 5*dp[f5])
            dp.append(x)
            if 2*dp[f2]==x: f2 += 1
            if 3*dp[f3]==x: f3 += 1
            if 5*dp[f5]==x: f5 += 1
        return dp[-1]