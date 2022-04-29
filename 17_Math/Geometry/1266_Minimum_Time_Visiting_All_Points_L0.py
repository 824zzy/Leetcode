""" https://leetcode.com/problems/minimum-time-visiting-all-points/
the minimum time between two points: max(dx, dy)
"""
class Solution:
    def minTimeToVisitAllPoints(self, A: List[List[int]]) -> int:
        ans = 0
        for i in range(len(A)-1):
            x0, y0 = A[i]
            x1, y1 = A[i+1]
            dx, dy = abs(x0-x1), abs(y0-y1)
            ans += max(dx, dy)
        return ans