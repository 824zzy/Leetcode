""" https://leetcode.com/problems/rotting-oranges/
count fresh oranges to impossible case.
count steps by bfs, no need to use seen
"""
from header import *

class Solution:
    def orangesRotting(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        Q = [(i, j) for j in range(N) for i in range(M) if A[i][j]==2]
        fresh = sum([1 for j in range(N) for i in range(M) if A[i][j]==1])
        if not fresh: return 0
        
        step = -1
        while Q:
            for _ in range(len(Q)):
                x, y = Q.pop(0)
                for dx, dy in D:
                    if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]==1:
                        Q.append([x+dx, y+dy])
                        A[x+dx][y+dy] = 2
                        fresh -= 1
            step += 1

        if not fresh: return step
        else: return -1