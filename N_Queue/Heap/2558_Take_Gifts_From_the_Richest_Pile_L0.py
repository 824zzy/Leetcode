""" https://leetcode.com/problems/take-gifts-from-the-richest-pile/
greedily get maximum gift from each pile, and put back the square root of the gift
"""
from header import *

class Solution:
    def pickGifts(self, A: List[int], k: int) -> int:
        A = [-x for x in A]
        heapify(A)
        for _ in range(k):
            mx = -heappop(A)
            rm = int(sqrt(mx))
            heappush(A, -rm)
        return -sum(A)
            