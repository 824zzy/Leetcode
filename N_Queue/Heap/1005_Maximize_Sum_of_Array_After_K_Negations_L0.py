""" https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
use heap to simulate the process of negation
"""
class Solution:
    def largestSumAfterKNegations(self, A: List[int], k: int) -> int:
        heapify(A)
        for _ in range(k):
            heappush(A, -heappop(A))
        return sum(A)