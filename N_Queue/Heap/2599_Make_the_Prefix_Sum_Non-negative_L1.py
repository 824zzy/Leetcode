""" https://leetcode.com/problems/make-the-prefix-sum-non-negative/
once the prefix sum is negative, we need to make it non-negative by pop the smallest element from the heap
"""
from header import *

class Solution:
    def makePrefSumNonNegative(self, A: List[int]) -> int:
        ans = 0
        sm = 0
        pq = []
        for x in A:
            sm += x
            heappush(pq, x)
            if sm<0:
                sm -= heappop(pq)
                ans += 1
        return ans
            
        
        
        
"""
[2,3,-5,4]
[3,-5,-2,6]
[6,-6,-3,3,1,5,-4,-3,-2,-3,4,-1,4,4,-2,6,0]
"""