""" https://leetcode.com/problems/furthest-building-you-can-reach/
When we are run out of bricks, we need to use a ladder to replace the bricks for the minimal height difference.
"""
from header import *

class Solution:
    def furthestBuilding(self, A: List[int], b: int, l: int) -> int:
        pq = []
        for i in range(len(A)-1):
            if A[i]>=A[i+1]: 
                continue
            diff = A[i+1]-A[i]
            heappush(pq, -diff)
            b -= diff
            if b<0:
                if l==0:
                    return i
                b += -heappop(pq)
                l -= 1
        return len(A)-1