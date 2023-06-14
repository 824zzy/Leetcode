""" https://leetcode.com/problems/maximum-sum-queries/
ZKW segment tree
"""
from header import *

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.T = [-1]*2*self.n

    def _set(self, i, val):
        i += self.n
        while i:
            self.T[i] = max(val, self.T[i])
            i //= 2

    def rangeMax(self, l, r):
        ans = -1
        l, r = l+self.n, r+self.n
        while l<=r:
            if l%2: ans, l = max(ans, self.T[l]), l+1 # if l is right child
            if not r%2: ans, r = max(ans, self.T[r]), r-1 # if r is left child
            l, r = l//2, r//2
        return ans
        
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        v2i = {x: i for i, x in enumerate(sorted(set(nums2+[y for _, y in queries])))}
        A = sorted(zip(nums1, nums2), reverse=True)
        queries = sorted([q+[i] for i, q in enumerate(queries)], reverse=True)
        ST = SegmentTree(len(v2i)+1)
        ans = [-1]*len(queries)
        j = 0
        for x, y, i in queries:
            while j<len(A) and x<=A[j][0]:
                ST._set(v2i[A[j][1]], A[j][0]+A[j][1])
                j += 1
            ans[i] = ST.rangeMax(v2i[y], len(v2i))
        return ans