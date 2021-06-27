""" L1
is_island = is_island & dfs(x+dx, y+dy)
"""
class Solution:
    def countSubIslands(self, A: List[List[int]], B: List[List[int]]) -> int:
        neibs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        M, N = len(B), len(B[0])
        ans = 0
        
        def dfs(x, y):
            B[x][y] = 0
            is_island = A[x][y]
            for dx, dy in neibs:
                if 0<=x+dx<M and 0<=y+dy<N and B[x+dx][y+dy]==1:
                    is_island = is_island & dfs(x+dx, y+dy)
            return is_island
            
        
        for i in range(M):
            for j in range(N):
                if B[i][j]==1 and A[i][j]==1:
                    if dfs(i, j): 
                        ans += 1
        return ans