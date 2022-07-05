""" https://leetcode.com/problems/ugly-number/
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0: return False
        
        @cache
        def dp(n):
            if n==1: return True
            ans = False
            for x in (2,3,5):
                if n%x==0:
                    ans |= dp(n//x)
            return ans
            
        return dp(n)