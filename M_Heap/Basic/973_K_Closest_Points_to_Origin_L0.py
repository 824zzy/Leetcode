""" https://leetcode.com/problems/k-closest-points-to-origin/
build heap based on distance to origin
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        A = []
        for x, y in points:
            heapq.heappush(A, (x**2+y**2, [x, y]))
        return [heapq.heappop(A)[1] for _ in range(k)]