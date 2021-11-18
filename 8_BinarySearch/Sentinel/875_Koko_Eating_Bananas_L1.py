""" https://leetcode.com/problems/koko-eating-bananas/
can eat m in H hours as sentinel
"""
class Solution:
    def minEatingSpeed(self, A: List[int], H: int) -> int:
        def can_eat(m):
            h = 0
            for a in A:
                h += ceil(a/m)
                if h>H: return False
            return True
        
        l, r = 1, max(A)
        while l<=r:
            m = (l+r)//2
            if not can_eat(m): l = m+1
            else: r = m-1
        return l