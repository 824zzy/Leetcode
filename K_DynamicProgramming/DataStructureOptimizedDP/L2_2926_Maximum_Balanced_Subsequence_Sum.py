""" https://leetcode.com/problems/maximum-balanced-subsequence-sum/
A[i]-A[j] >= i-j ==> A[i]-i >= A[j]-j
"""
from header import *

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [0]*2*self.n

    def _set(self, i, val):
        i += self.n
        while i:
            self.T[i] = max(val, self.T[i])
            i //= 2
    
    def rangeMax(self, l, r):
        ans = 0
        l, r = l+self.n, r+self.n
        while l<=r:
            if l%2: ans, l = max(ans, self.T[l]), l+1 # if l is right child
            if not r%2: ans, r = max(ans, self.T[r]), r-1 # if r is left child
            l, r = l//2, r//2
        return ans
    
class Solution:
    def maxBalancedSubsequenceSum(self, A: List[int]) -> int:
        B = sorted(set(x-i for i, x in enumerate(A)))
        ST = SegmentTree(len(B)+1)
        ans = -inf
        for i, x in enumerate(A):
            j = bisect_left(B, x-i)+1
            mx = ST.rangeMax(0, j)+x
            ans = max(ans, mx)
            ST._set(j, mx)
        return ans