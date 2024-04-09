""" https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
use k as threshold to maintain heap H
"""


class Solution:
    def kthSmallest(self, A: List[List[int]], k: int) -> int:
        H = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                heapq.heappush(H, -A[i][j])
                if len(H) > k:
                    heapq.heappop(H)
        return -heapq.heappop(H)
