""" https://leetcode.com/problems/maximal-score-after-applying-k-operations/
simulate by heap
"""
from header import *


class Solution:
    def maxkelements(self, A: List[int], k: int) -> int:
        A = [-x for x in A]
        heapify(A)
        ans = 0
        for _ in range(k):
            x = heappop(A)
            ans -= x
            heappush(A, floor(x / 3))
        return ans
