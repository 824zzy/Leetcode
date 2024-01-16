""" https://leetcode.com/problems/shortest-distance-from-all-buildings/
bfs + simulation
"""
from header import *

class Solution:
    def shortestDistance(self, G: List[List[int]]) -> int:
        m, n = len(G), len(G[0])
        B = [(i, j) for i in range(m) for j in range(n) if G[i][j]==1]
        D = [[[inf]*len(B) for j in range(n)] for i in range(m)]
        for i, (sx, sy) in enumerate(B):
            step = 1
            Q = [(sx, sy)]
            seen = {(sx, sy)}
            while Q:
                nxtQ = []
                for x, y in Q:
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        if 0<=x+dx<m and 0<=y+dy<n and G[x+dx][y+dy]==0 and (x+dx, y+dy) not in seen:
                            seen.add((x+dx, y+dy))
                            nxtQ.append((x+dx, y+dy))
                            D[x+dx][y+dy][i] = step
                Q = nxtQ
                step += 1
        ans = min([sum(D[i][j]) for i in range(m) for j in range(n)])
        return ans if ans!=inf else -1
        
        