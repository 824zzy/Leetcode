""" https://leetcode.com/problems/take-gifts-from-the-richest-pile/
greedily get maximum gift from each pile, and put back the square root of the gift
"""
from header import *

# heapreplace is preferred for performance
class Solution:
    def pickGifts(self, A: List[int], k: int) -> int:
        A = [-x for x in A]
        heapify(A)
        for _ in range(k):
            heapreplace(A, -int(sqrt(-A[0])))
        return -sum(A)


class Solution:
    def pickGifts(self, A: List[int], k: int) -> int:
        A = [-x for x in A]
        heapify(A)
        for _ in range(k):
            mx = -heappop(A)
            rm = int(sqrt(mx))
            heappush(A, -rm)
        return -sum(A)
