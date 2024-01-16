""" https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
sort the properties and maintain monotonic decreasing stack
"""
from header import *

# readable version
class Solution:
    def numberOfWeakCharacters(self, P: List[List[int]]) -> int:
        P.sort(key=lambda x: (x[0], -x[1]))
        A = [x[1] for x in P]
        
        # next greater to the right
        R = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]<A[i]:
                R[stk.pop()] = i
            stk.append(i)
            
        ans = 0
        for i, x in enumerate(R):
            if x!=len(A):
                ans += 1
        return ans


class Solution:
    def numberOfWeakCharacters(self, P: List[List[int]]) -> int:
        P.sort(key=lambda x: (x[0], -x[1]))
        stk = []
        ans = 0
        for i, (_, d) in enumerate(P):
            while stk and P[stk[-1]][1]<d:
                stk.pop()
                ans += 1
            stk.append(i)
        return ans