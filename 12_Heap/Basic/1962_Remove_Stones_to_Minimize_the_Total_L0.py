""" https://leetcode.com/problems/remove-stones-to-minimize-the-total/
1. use a max-heap to greedily find the maximal value
2. update the heap by maximal value and return the sum of heap
"""
class Solution:
    def minStoneSum(self, A: List[int], k: int) -> int:
        A = list(map(lambda x: -x, A))
        heapq.heapify(A)
        for _ in range(k):
            ma = heapq.heappop(A)
            heapq.heappush(A, ma//2)
        return -sum(A)