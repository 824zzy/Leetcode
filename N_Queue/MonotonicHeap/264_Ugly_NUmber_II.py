""" https://leetcode.com/problems/ugly-number-ii/
maintain priority queue to iteratively find next ugly number
"""

from header import *


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = [1]
        heapify(pq)
        seen = {1}
        for _ in range(n - 1):
            x = heappop(pq)
            for f in 2, 3, 5:
                if x * f not in seen:
                    heappush(pq, x * f)
                    seen.add(x * f)
        return heappop(pq)
