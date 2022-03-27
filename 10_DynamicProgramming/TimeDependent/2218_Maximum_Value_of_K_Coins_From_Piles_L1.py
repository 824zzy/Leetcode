""" https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
from lee: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/discuss/1887010/JavaC%2B%2BPython-Top-down-DP-solution
dp[i,k] means picking k elements from pile[i] to pile[n-1].
We can pick 0,1,2,3... elements from the current pile[i] one by one.
It asks for the maximum total value of coins we can have,
so we need to return max of all the options.
"""
class Solution:
    def maxValueOfCoins(self, A: List[List[int]], k: int) -> int:    
        @cache
        def dp(i, k):
            if k==0 or i==len(A): return 0
            ans = dp(i+1, k)
            val = 0
            
            for j in range(min(len(A[i]), k)):
                val += A[i][j]
                ans = max(ans, val+dp(i+1, k-j-1))
            return ans
                    
        return dp(0, k)