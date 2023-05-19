""" https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
brute force by bit mask, this solution can be optimized.
"""
class Solution:
    def minSessions(self, A: List[int], T: int) -> int:
        @cache
        def dp(mask, t):
            if mask==(1<<len(A))-1: return 0
            ans = inf
            for i in range(len(A)):
                if not mask&(1<<i):
                    if A[i]<=t:
                        ans = min(ans, dp(mask^(1<<i), t-A[i]))
                    else:
                        ans = min(ans, 1 + dp(mask^(1<<i), T-A[i]))
            return ans
        
        return dp(0, 0)