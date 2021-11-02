""" L2: https://leetcode.com/problems/non-overlapping-intervals/
maintain monotonic increasing priority queue by s>=-1*pq[0]
"""
class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: x[1])
        pq = [-A[0][1]]
        for s, e in A[1:]:
            if s>=-1*pq[0]:
                heappush(pq, -e)
        return len(A)-len(pq)