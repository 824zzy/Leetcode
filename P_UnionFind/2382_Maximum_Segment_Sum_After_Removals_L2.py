""" https://leetcode.com/problems/maximum-segment-sum-after-removals/submissions/
The Disjoint Set(or Union-Find) class template is universal. For this specific problem, one observation is we can maintain segments from the end to the start of the queries to find the maximum segment sum.

Since the template only gives us information about whether two elements belong to the same group, the only tricky part is how to keep track of the size information. So we need a Counter `segments` for creating a new group and merging existing groups.
"""
from header import *

class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution:
    def maximumSegmentSum(self, A: List[int], Q: List[int]) -> List[int]:
        dsu = DSU(len(A))
        ans, mx, segments = [], 0, Counter()
        for x in reversed(Q):
            ans.append(mx)
            l, r = 0, 0
            if x+1<len(A):
                r = segments[dsu.find(x+1)]
                if r:
                    dsu.union(x, x+1)
                    segments.pop(dsu.find(x+1))
            if x-1>=0:
                l = segments[dsu.find(x-1)]
                if l:
                    dsu.union(x, x-1)
                    segments.pop(dsu.find(x-1))
            segments[dsu.find(x)] += l+r+A[x]
            mx = max(mx, segments[dsu.find(x)])
        return ans[::-1]