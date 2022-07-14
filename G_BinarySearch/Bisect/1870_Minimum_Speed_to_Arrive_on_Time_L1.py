""" https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
binary search on the speed, and check if the time sum is valid.
"""
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def fn(speed):
            sm = 0
            for i, x in enumerate(dist):
                if i<len(dist)-1: sm += ceil(x/speed)
                else: sm += x/speed
                if sm>hour: return False
            return True
                
        
        l, r = 1, 10**7+1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l if l!=(10**7+1) else -1