""" https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/
searching answer by bfs
"""
from header import *

class Solution:
    def findMaxFish(self, G: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0
        for i in range(len(G)):
            for j in range(len(G[0])):
                if G[i][j]:
                    Q = [(i, j, G[i][j])]
                    G[i][j] = 0
                    _ans = 0
                    while Q:
                        x, y, fish = Q.pop(0)
                        _ans += fish
                        for dx, dy in D:
                            if 0<=x+dx<len(G) and 0<=y+dy<len(G[0]) and G[x+dx][y+dy]:
                                tmp = G[x+dx][y+dy]
                                G[x+dx][y+dy] = 0
                                Q.append((x+dx, y+dy, tmp))
                    ans = max(ans, _ans)
        return ans
    

"""
[[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
[[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
[[10,5],[8,0]]
[[5,0,0,8],[2,0,0,0]]
"""