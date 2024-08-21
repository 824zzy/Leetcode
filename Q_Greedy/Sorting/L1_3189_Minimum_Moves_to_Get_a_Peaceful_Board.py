""" https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/
greedily assign rows and columns for each rook
"""

from header import *


class Solution:
    def minMoves(self, G: List[List[int]]) -> int:
        G.sort()
        # assign rows
        ans = 0
        for i, (x, y) in enumerate(G):
            ans += abs(i - x)
            G[i] = [i, y]
        G.sort(key=lambda x: x[1])
        # assign columns
        for i, (x, y) in enumerate(G):
            ans += abs(i - y)
        return ans


"""
[[0,0],[1,0],[1,1]]
[[0,0],[0,1],[0,2],[0,3]]
[[0,0],[1,3],[4,1],[2,4],[2,0]]
"""
