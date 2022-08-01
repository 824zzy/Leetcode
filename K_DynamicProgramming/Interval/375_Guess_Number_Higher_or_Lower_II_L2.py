""" https://leetcode.com/problems/guess-number-higher-or-lower-ii/
"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(l, r):
            if l>=r: return 0
            ans = inf
            for m in range(l, r+1):
                ans = min(ans, m+max(dp(l, m-1), dp(m+1, r)))
            return ans
        
        return dp(1, n)