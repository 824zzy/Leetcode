""" https://leetcode.com/problems/maximum-subarray-min-product/
1. scan two pass to find next smaller on the left and right by monotonic increasing stack
2. for each A[i] as minimum, find the maximum subarray min-Product by largest span and prefix sum

similar to 907, 2281
"""
from header import *

class Solution:
    def maxSumMinProduct(self, A: List[int]) -> int:
        # find next smaller element's index on the right
        R = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>A[i]:
                R[stk.pop()] = i
            stk.append(i)
            
        # find next smaller element's index on the left
        L = [-1]*len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]>=A[i]:
                L[stk.pop()] = i
            stk.append(i)
            
        # compute prefix sum and the largest span for max_min-product
        prefix = list(accumulate(A, initial=0))
        ans = -inf
        for i, (l, r) in enumerate(zip(L, R)):
            ans = max(ans, A[i]*(prefix[r]-prefix[l+1]))
        return ans%(10**9+7)