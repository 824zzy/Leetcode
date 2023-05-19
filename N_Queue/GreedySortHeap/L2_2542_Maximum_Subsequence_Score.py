""" https://leetcode.com/problems/maximum-subsequence-score/
the same as 857. Minimum Cost to Hire K Workers
"""
from header import *

class Solution:
    def maxScore(self, A: List[int], B: List[int], k: int) -> int:
        A = sorted(zip(A, B), key=lambda x: -x[1])
        pq = [x for x, _ in A[:k]]
        heapify(pq)
        sm = sum(pq)
        ans = sum(pq)*A[k-1][1]
        for a, b in A[k:]:
            sm += a - heapreplace(pq, a)
            ans = max(ans, sm*b)
        return ans