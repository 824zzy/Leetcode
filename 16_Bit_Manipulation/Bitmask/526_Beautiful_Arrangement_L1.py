""" https://leetcode.com/problems/beautiful-arrangement/
Start from 0 mask, if i-th number hasn't been selected yet and follows the rules.
Then fill it on mask and check the next place.
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(mask, idx):
            if idx==n+1: return 1
            
            ans = 0
            for i in range(n):
                if not mask & 1<<i:
                    if ((i+1)%idx==0 or idx%(i+1)==0):
                        ans += dfs(mask ^ 1<<i, idx+1)
            return ans
        
        return dfs(0, 1)