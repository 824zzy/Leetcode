""" L1: https://leetcode.com/problems/surrounded-regions/
Flood fill Os from the boundary with a sentinel # to mark that this O is not surrounded. 
Traverse the board and replace O with X and # with O.
"""
class Solution:
    def solve(self, A: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(A), len(A[0])
        D = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def bfs(x, y):
            Q = [[x, y]]
            A[x][y] = '#'
            while Q:
                x, y = Q.pop(0)
                for dx, dy in D:
                    if 0<x+dx<M-1 and 0<y+dy<N-1 and A[x+dx][y+dy]=='O':
                        A[x+dx][y+dy] = '#'
                        Q.append([x+dx, y+dy])
                
        for i in range(M):
            for j in range(N):
                if (i in [0, M-1] or j in [0, N-1]) and A[i][j]=='O': bfs(i, j)
                    
        for i in range(M):
            for j in range(N):
                if A[i][j]=='O': A[i][j] = 'X'
                if A[i][j]=='#': A[i][j] = 'O'