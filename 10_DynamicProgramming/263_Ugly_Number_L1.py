""" https://leetcode.com/problems/ugly-number/
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0: return False
        
        @cache
        def dfs(n):
            if n==1: return True
            return any([dfs(n//f) for f in [2, 3, 5] if n%f==0])
            
        return dfs(n)