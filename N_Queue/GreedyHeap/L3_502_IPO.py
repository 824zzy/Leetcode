""" https://leetcode.com/problems/ipo/
1. sort the profits and capital
2. use priority queue to greedily finding top k maximum profit
"""
from header import *


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        A = sorted(list(zip(capital, profits)))
        ans = w
        i = 0
        pq = []

        for _ in range(k):
            while i < len(A) and A[i][0] <= ans:
                heappush(pq, -A[i][1])
                i += 1
            if pq:
                ans -= heappop(pq)
        return ans
