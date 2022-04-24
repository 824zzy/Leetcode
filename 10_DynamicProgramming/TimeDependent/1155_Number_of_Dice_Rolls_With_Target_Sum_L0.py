""" https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
use dp to find all summations of every roll up to n

Time: O(n*k)
"""
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(i, sm):
            if i==n:
                if sm==target: return 1
                else: return 0
            
            ans = 0
            for x in range(1, k+1): 
                ans += dp(i+1, sm+x)
            return ans
        
        return dp(0, 0)%(10**9+7)