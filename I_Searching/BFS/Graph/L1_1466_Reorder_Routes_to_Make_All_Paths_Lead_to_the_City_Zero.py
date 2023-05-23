""" https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
bfs to count in-degrees
"""
from header import *

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        G = defaultdict(dict)
        for i, j in connections:
            G[i][j] = False
            G[j][i] = True
            
        Q = [0]
        seen = {0}
        ans = 0
        while Q:
            i = Q.pop(0)
            for j in G[i]:
                if j not in seen:
                    Q.append(j)
                    seen.add(j)
                    if G[i][j]==False: ans += 1
        return ans