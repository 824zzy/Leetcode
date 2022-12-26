""" https://leetcode.com/problems/maximum-tastiness-of-candy-basket/
Looking for max-mini ==> binary search

In the search function, greedily select candies
"""
from header import *

class Solution:
    def maximumTastiness(self, A: List[int], k: int) -> int:
        def fn(x):
            pre = A[0]
            cnt = 1
            for i in range(1, len(A)):
                if A[i]-pre>=x:
                    pre = A[i]
                    cnt += 1
            return cnt<k
                
        A.sort()
        l, r = 0, A[-1]-A[0]+1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l-1
        
"""
[1, 2, 5, 8, 13, 21]
"""