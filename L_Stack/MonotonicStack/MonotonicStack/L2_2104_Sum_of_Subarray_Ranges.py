""" https://leetcode.com/problems/sum-of-subarray-ranges/
This problem is labeled as medium simply for the sake of low time limitation.
If the size of nums becomes 10**4, only monotonic stack solution is acceptable.

For monotonic stack solution, it is essentially the same as 907.
"""
from header import *

# O(N)
class Solution:
    def subArrayRanges(self, A: List[int]) -> int:
        # next smaller&larger on the right
        R_min = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>A[i]:
                R_min[stk.pop()] = i
            stk.append(i)
            
        R_max = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]<A[i]:
                R_max[stk.pop()] = i
            stk.append(i)
        
        # next smaller&larger on the left
        L_min = [-1]*len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]>=A[i]:
                L_min[stk.pop()] = i
            stk.append(i)
            
        L_max = [-1]*len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]<=A[i]:
                L_max[stk.pop()] = i
            stk.append(i)
            
        # for each A[i] as minimum and maximum, compute their sums
        min_sum = 0
        for i, (l, r) in enumerate(zip(L_min, R_min)):
            min_sum += A[i] * (i-l) * (r-i)
        
        max_sum = 0
        for i, (l, r) in enumerate(zip(L_max, R_max)):
            max_sum += A[i] * (i-l) * (r-i)
        
        return max_sum-min_sum
    
# O(N^2)
class Solution:
    def subArrayRanges(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            ma, mi = -inf, inf
            for j in range(i, len(A)):
                ma, mi = max(ma, A[j]), min(mi, A[j])
                ans += ma-mi
        return ans