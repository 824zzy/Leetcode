""" https://leetcode.com/problems/last-stone-weight/
"""
class Solution:
    def lastStoneWeight(self, S: List[int]) -> int:
        A = list(map(lambda x: -x, A))
        heapq.heapify(A)
        while len(A)>1:
            i = heapq.heappop(A)
            j = heapq.heappop(A)
            heapq.heappush(A, -abs(i-j))
        return -A[0]