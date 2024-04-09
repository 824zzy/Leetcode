""" https://leetcode.com/problems/maximum-performance-of-a-team/
1. sort the engineers by their efficiency
2. greedily add k engineer with highest efficiency to the team by heap
"""
from header import *


class Solution:
    def maxPerformance(
            self,
            n: int,
            speed: List[int],
            efficiency: List[int],
            k: int) -> int:
        A = list(zip(speed, efficiency))
        A.sort(key=lambda x: -x[1])

        pq = []
        sm = 0
        ans = 0
        for s, e in A:
            heappush(pq, s)
            sm += s
            if len(pq) > k:
                sm -= heappop(pq)
            ans = max(ans, sm * e)
        return ans % (10**9 + 7)
