""" L1: https://leetcode.com/problems/grid-game/
It is a min-max problem: find minimal maximized the prefix or suffix.
The inspiration is the first robot only move down once due to the 2 by n grid.

robot 2 optimal chose: max(pre_down[i], suf_up[i+1])
robot 1 optimal chose: min(ans, robot2 choose)
"""


class Solution:
    def gridGame(self, A: List[List[int]]) -> int:
        ans = float("inf")
        prefix = 0
        suffix = sum(A[0])
        for i in range(len(A[0])):
            suffix -= A[0][i]
            ans = min(ans, max(prefix, suffix))
            prefix += A[1][i]
        return ans


class Solution:
    def gridGame(self, A: List[List[int]]) -> int:
        suf_up = list(accumulate(reversed(A[0]), initial=0))[::-1]
        pre_down = list(accumulate(A[1], initial=0))

        ans = inf
        for i in range(len(A[0])):
            ans = min(ans, max(pre_down[i], suf_up[i + 1]))
        return ans
