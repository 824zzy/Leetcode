""" https://leetcode.com/problems/minimum-knight-moves/
simulation using bfs
"""
class Solution:
    def minKnightMoves(self, tx: int, ty: int) -> int:
        Q = [(0, 0, 0)]
        seen = {(0, 0)}
        
        while Q:
            nxtQ = Q
            for x, y, step in Q:
                if x==tx and y==ty:
                    return step
                for dx, dy in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1), (-1, -2), (-2, -1)):
                    if (x+dx, y+dy) not in seen:
                        seen.add((x+dx, y+dy))
                        nxtQ.append((x+dx, y+dy, step+1))
            Q = nxtQ