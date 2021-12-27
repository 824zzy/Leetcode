""" https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""
class Solution:
    def shipWithinDays(self, A: List[int], days: int) -> int:    
        def feasible(m):
            w, d = 0, 1
            for x in A:
                if w+x>m:
                    d, w = d+1, 0
                    if d>days: return False
                w += x
            return True
                    
        
        l, r = max(A), sum(A)
        while l<=r:
            m = (l+r)//2
            if not feasible(m): l = m + 1
            else: r = m - 1
        return l