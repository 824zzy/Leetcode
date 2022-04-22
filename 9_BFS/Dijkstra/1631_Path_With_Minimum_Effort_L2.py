""" https://leetcode.com/problems/path-with-minimum-effort/
use coordinate as key for seen.
"""
class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = [(0, 0, 0)]
        seen = {(0, 0): 0}
        
        while pq:
            h, x, y = heappop(pq)
            if x==M-1 and y==N-1: return h
            for dx, dy in D:
                if 0<=x+dx<M and 0<=y+dy<N:
                    hh = max(h, abs(A[x+dx][y+dy]-A[x][y]))
                    if (x+dx, y+dy) not in seen or hh<seen[(x+dx, y+dy)]:
                        heappush(pq, (hh, x+dx, y+dy))
                        seen[x+dx, y+dy] = hh