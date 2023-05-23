""" https://leetcode.com/problems/shortest-path-in-binary-matrix
Simply use bfs to find shortest path. 
Dijkstra algorithm is not necessary since all the edge weights are exactly 1.
"""
class Solution:
    def shortestPathBinaryMatrix(self, G: List[List[int]]) -> int:
        if G[0][0]==1: return -1
        
        D = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        Q = [(1, 0, 0)]
        seen = set()
        
        while Q:
            cost, x, y = Q.pop(0)
            if (x, y)==(len(G)-1, len(G[0])-1): return cost
            if (x, y) not in seen:
                seen.add((x, y))
                for dx, dy in D:
                    if 0<=x+dx<len(G) and 0<=y+dy<len(G[0]) and G[x+dx][y+dy]==0:
                        Q.append((cost+1, x+dx, y+dy))
        return -1