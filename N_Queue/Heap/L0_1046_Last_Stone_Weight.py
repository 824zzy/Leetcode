""" https://leetcode.com/problems/last-stone-weight/
simulate using heap
"""

from header import *


class Solution:
    def lastStoneWeight(self, A: List[int]) -> int:
        A = [-x for x in A]
        heapify(A)
        for i in range(len(A) - 1):
            x = -heappop(A)
            y = -heappop(A)
            heappush(A, y - x)
        return -A[0]
