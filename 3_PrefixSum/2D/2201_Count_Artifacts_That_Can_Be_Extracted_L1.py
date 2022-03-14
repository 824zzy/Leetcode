""" https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
1. compute the 2D prefix sum of digged cell
2. compare the area of artifacts and digged cells
"""
class Solution:
    def digArtifacts(self, n: int, A: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(n)]
        for i, j in dig: grid[i][j] = 1
        
        prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(n): 
                prefix[i+1][j+1] = grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
        
        ans = 0
        for r1, c1, r2, c2 in A:
            area = prefix[r2+1][c2+1]-prefix[r2+1][c1]-prefix[r1][c2+1]+prefix[r1][c1]
            if area==(r2+1-r1)*(c2+1-c1): ans += 1
        return ans