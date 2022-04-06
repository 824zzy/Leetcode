""" https://leetcode.com/problems/word-search/
"""
class Solution:
    def exist(self, A: List[List[str]], word: str) -> bool:
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(A), len(A[0])
        
        def dfs(x, y, idx):
            if idx==len(word): return True
            
            for dx, dy in D:
                if 0<=x+dx<M and 0<=y+dy<N and A[x+dx][y+dy]==word[idx]:
                    tmp = A[x][y]
                    A[x][y] = ''
                    if dfs(x+dx, y+dy, idx+1): return True
                    A[x][y] = tmp
            return False
                    
        for i in range(M):
            for j in range(N):
                if A[i][j]==word[0]:
                    if dfs(i, j, 1): return True
        return False