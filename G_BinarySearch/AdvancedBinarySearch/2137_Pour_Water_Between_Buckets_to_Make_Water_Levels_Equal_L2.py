""" https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/
1. use precision(1e-5) to decide if the answer is correct
2. use prefix sum(optimal) or liner scan to calculate the difference between x<m and x>m
"""
from header import *

class Solution:
    def equalizeWater(self, A: List[int], loss: int) -> float:        
        def fn(m):
            # return difference between x<m and x>m
            i = bisect_left(A, m)
            sm1 = i*m-presum[i]
            sm2 = presum[-1]-presum[i]-(len(presum)-i-1)*m
            return sm1>sm2*(100-loss)/100
                    
        A.sort()
        presum = list(accumulate(A, initial=0))
        l, r = A[0], sum(A)/len(A)
        while r-l>=1e-5:
            m = (l+r)/2
            if fn(m): r = m
            else: l = m
        return l


class Solution:
    def equalizeWater(self, A: List[int], loss: int) -> float:        
        def fn(m):
            sm1 = 0
            sm2 = 0
            for x in A:
                if x<m:
                    sm1 += m-x
                else:
                    sm2 += x-m
            return sm1>sm2*(100-loss)/100
        
        l, r = min(A), max(A)
        while r-l>=1e-5:
            m = (l+r)/2
            if fn(m): r = m
            else: l = m
        return l