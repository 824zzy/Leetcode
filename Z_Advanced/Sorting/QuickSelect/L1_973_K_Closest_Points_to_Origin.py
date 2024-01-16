""" https://leetcode.com/problems/k-closest-points-to-origin/
quick select
"""
from header import *

# quick select
class Solution:
    def kClosest(self, A: List[List[int]], k: int) -> List[List[int]]:
        def partition(l, r): 
            """Return partition of A[l:r]."""
            i, j = l+1, r-1
            while i<=j: 
                if A[i]<A[l]: i += 1
                elif A[j]>A[l]: j -= 1
                else: 
                    A[i], A[j] = A[j], A[i]
                    i, j = i+1, j-1
            A[l], A[j] = A[j], A[l]
            return j
        
        A = [(x*x+y*y, x, y) for x, y in A]
        shuffle(A)
        l, r = 0, len(A)
        while l<r:
            m = partition(l, r)
            if m+1<k: l = m + 1
            elif m+1==k: break
            else: r = m
        return [[x, y] for _, x, y in A if x*x+y*y<=A[m][0]]

# sort
class Solution:
    def kClosest(self, A: List[List[int]], k: int) -> List[List[int]]:
        A = sorted(A, key=lambda x: x[0]*x[0]+x[1]*x[1])
        return A[:k]

# heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        A = []
        for x, y in points:
            heappush(A, (x**2+y**2, [x, y]))
        return [heappop(A)[1] for _ in range(k)]
    
