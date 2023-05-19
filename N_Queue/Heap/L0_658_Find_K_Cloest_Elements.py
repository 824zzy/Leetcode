""" https://leetcode.com/problems/find-k-closest-elements/
straight-forward solution using heap
time complexity: O(nlogn)
"""
from header import *

class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        pq = []
        for a in A:
            heappush(pq, (abs(a-x), a))
        return sorted([heappop(pq)[1] for _ in range(k)])