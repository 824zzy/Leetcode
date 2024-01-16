""" https://leetcode.com/problems/buildings-with-an-ocean-view/
monotonic stack to find next greater on the right

greedily scan from right to left also works
"""
from header import *

class Solution:
    def findBuildings(self, A: List[int]) -> List[int]:
        n = len(A)
        R = [n]*(n)
        stk = []
        for i in range(n):
            while stk and A[stk[-1]]<=A[i]:
                R[stk.pop()] = i
            stk.append(i)
        return [i for i, x in enumerate(R) if x==n]
            
            
"""
[4,2,3,1]
[4,3,2,1]
[1,3,2,4]
[2,2,2,2]
"""