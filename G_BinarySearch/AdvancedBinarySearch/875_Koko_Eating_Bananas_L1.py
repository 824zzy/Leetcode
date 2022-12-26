""" https://leetcode.com/problems/koko-eating-bananas/
check if Koko can eat m bananas in H hours as sentinel
"""
class Solution:
    def minEatingSpeed(self, A: List[int], h: int) -> int:
        def fn(m, h):
            cnt = 0
            for x in A:
                cnt += ceil(x/m)
            return cnt<=h
        
        l, r = 1, max(A)
        while l<r:
            m = (l+r)//2
            if fn(m, h): r = m
            else: l = m + 1
        return l