""" https://leetcode.com/problems/cherry-pickup/
Imagine we have two robots starting at 0, 0 and collecting cherries at the same time. The purpose is to collect most cherries possible using these two robots.

Define fn(t, i, ii) as the maximum cherries collected at time t when the two robots are at i and iith rows. Then,

fn(t, i, ii) = grid[i][j] + (i != ii)*grid[ii][jj] + max(fn(t-1, i-1, ii-1), fn(t-1, i-1, ii), fn(t-1, i, ii-1), fn(t-1, i, ii)).

Time: O(n^3)
"""


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @cache
        def fn(t, i, ii):
            """Return maximum cherries collected at kth step when two robots are at ith and iith row"""
            j, jj = t - i, t - ii  # columns
            if not (0 <= i < n and 0 <= j < n) or t < i or grid[i][j] == -1:
                return -inf  # robot 1 not at proper location
            if not (0 <= ii < n and 0 <= jj <
                    n) or t < ii or grid[ii][jj] == -1:
                return -inf  # robot 2 not at proper location
            if t == 0:
                return grid[0][0]  # starting from 0,0
            return grid[i][j] + (i != ii) * grid[ii][jj] + max(fn(t - 1, x, y)
                                                               for x in (i - 1, i) for y in (ii - 1, ii))

        return max(0, fn(2 * n - 2, n - 1, n - 1))
