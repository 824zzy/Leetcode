""" https://leetcode.com/problems/max-value-of-equation/
Since the target to be optimized is yi + yj + |xi - xj| (aka xj + yj + yi - xi given j > i), the value of interest is yi - xi.
So we can maintain a monotonic queue of (xi, yi - xi) and for each j, we can find the maximum value of yi - xi + xj + yj.
"""
from header import *

# heap implementation


class Solution:
    def findMaxValueOfEquation(self, A: List[List[int]], k: int) -> int:
        ans = -inf
        pq = []
        for xj, yj in A:
            while pq and xj - pq[0][1] > k:
                heappop(pq)
            if pq:
                ans = max(ans, xj + yj - pq[0][0])
            heappush(pq, (xj - yj, xj))
        return ans

# deque implementation


class Solution:
    def findMaxValueOfEquation(self, A: List[List[int]], k: int) -> int:
        dq = deque()
        ans = -inf

        for i, (x, y) in enumerate(A):
            while dq and x - dq[0][0] > k:
                dq.popleft()
            if dq:
                ans = max(ans, dq[0][1] + y + x - dq[0][0])
            while dq and dq[-1][1] - dq[-1][0] < y - x:
                dq.pop()
            dq.append((x, y))
        return ans
