""" https://leetcode.com/problems/minimum-time-to-complete-trips/
binary search to minimum time, note that the upper bound is to use the fastest bus to complete all trips
"""
class Solution:
    def minimumTime(self, A: List[int], T: int) -> int:
        def fn(m):
            ans = 0
            for x in A:
                ans += m // x
            return ans>=T
            
        l, r = 1, min(A)*T
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m + 1
        return l