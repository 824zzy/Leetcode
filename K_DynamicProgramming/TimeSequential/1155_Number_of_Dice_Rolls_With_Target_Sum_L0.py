""" https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
i-th state is only related i+1-th state from x==1 to x==k+1
"""
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(i, sm):
            if i==n: return sm==target
            ans = 0
            for x in range(1, k+1):
                ans += dp(i+1, sm+x)
            return ans
        
        return dp(0, 0)%(10**9+7)