""" https://leetcode.com/problems/remove-stones-to-minimize-the-total/
greedy: use a max-heap to greedily find the maximal value

1. use a max-heap to greedily find the maximal value
2. update the heap by maximal value and return the sum of heap
"""
from header import *


class Solution:
    def minStoneSum(self, A: List[int], k: int) -> int:
        A = [-x for x in A]
        heapify(A)
        for _ in range(k):
            mx = -heappop(A)
            heappush(A, -(mx - mx // 2))
        return -sum(A)
