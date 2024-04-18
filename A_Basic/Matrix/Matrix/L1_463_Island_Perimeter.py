""" https://leetcode.com/problems/island-perimeter/
counting the perimeter for each land cell
"""
from header import *


class Solution:
    def islandPerimeter(self, G: List[List[int]]) -> int:
        ans = 0
        for x in range(len(G)):
            for y in range(len(G[0])):
                if G[x][y] == 1:
                    ans += 4
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= x+dx < len(G) and 0 <= y+dy < len(G[0]) and G[x+dx][y+dy]:
                            ans -= 1
        return ans
