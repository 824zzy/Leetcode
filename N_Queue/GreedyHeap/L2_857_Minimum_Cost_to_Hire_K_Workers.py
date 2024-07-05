""" https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
1. Sort the workers by their efficiency from low to high.
2. Greedily update the answer and sum of costs using heapreplace.
"""
from header import *


class Solution:
    def mincostToHireWorkers(self, Q: List[int], W: List[int], k: int) -> float:
        A = sorted([(q, w / q) for q, w in zip(Q, W)], key=lambda x: x[1])
        pq = [-q for q, _ in A[:k]]
        heapify(pq)
        sm = -sum(pq)
        ans = sm * A[k - 1][1]
        for q, r in A[k:]:
            sm += q + heapreplace(pq, -q)
            ans = min(ans, sm * r)
        return ans
