""" L1: https://leetcode.com/problems/grid-game/
It is a min-max problem: find minimal maximized the prefix or suffix.
The inspiration is the first robot only move down once due to the 2 by n grid.
"""
class Solution:
    def gridGame(self, A: List[List[int]]) -> int:
        ans = float('inf')
        prefix = 0
        suffix = sum(A[0])
        for i in range(len(A[0])):
            suffix -= A[0][i]
            ans = min(ans, max(prefix, suffix))
            prefix += A[1][i]
        return ans
