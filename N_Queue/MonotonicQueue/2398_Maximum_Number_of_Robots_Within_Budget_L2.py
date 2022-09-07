""" https://leetcode.com/problems/maximum-number-of-robots-within-budget/
binary search + monotonic queue

note that all the running cost is positive, so it is not necessary to use monotonic queue on runningCosts!
"""
from header import *

class Solution:
    def maximumRobots(self, C: List[int], R: List[int], budget: int) -> int:
        C = [0]+C
        R = list(accumulate(R, initial=0))
        
        def fn(k):
            pqC = []
            ans = 0
            for i in range(1, len(R)):
                while pqC and i-pqC[0][1]>=k:
                    heappop(pqC)
                heappush(pqC, (-C[i], i))
                if i>=k and pqC and -pqC[0][0]+k*(R[i]-R[i-k])<=budget:
                    return True
            return False
        
        l, r = 0, len(C)
        while l<r:
            m = (l+r)//2
            if not fn(m): r = m
            else: l = m + 1
        return l-1