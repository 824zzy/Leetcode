""" https://leetcode.com/problems/matrix-block-sum/
be careful when dealing with corner indexes
"""
class Solution:
    def matrixBlockSum(self, A: List[List[int]], k: int) -> List[List[int]]:
        # compute 2D prefix sum
        m, n = len(A), len(A[0])
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n): 
                prefix[i+1][j+1] = A[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
        
        # find 4 corners for ans
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n): 
                r0, r1 = max(0, i-k), min(m-1, i+k)
                c0, c1 = max(0, j-k), min(n-1, j+k)
                ans[i][j] = prefix[r1+1][c1+1] - prefix[r0][c1+1] - prefix[r1+1][c0] + prefix[r0][c0]
        return ans 