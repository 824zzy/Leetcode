""" https://leetcode.com/problems/maximum-star-sum-of-a-graph/description/
For each node, sort its neighbors in descending order and take k max valued neighbors.

Note that the time complexity is O(nlogn) instead of O(n^2*logn)
"""
from header import *


class Solution:
    def maxStarSum(self, A: List[int], edges: List[List[int]], k: int) -> int:
        G = defaultdict(list)
        for i, j in edges:
            if A[j] > 0:
                G[i].append(j)
            if A[i] > 0:
                G[j].append(i)

        ans = -inf
        for i, v in enumerate(A):
            neib = sorted([A[j] for j in G[i]], reverse=True)
            ans = max(ans, sum(neib[:k]) + v)
        return ans
