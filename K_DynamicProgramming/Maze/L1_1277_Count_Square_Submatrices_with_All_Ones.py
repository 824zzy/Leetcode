""" https://leetcode.com/problems/count-square-submatrices-with-all-ones/
The same as 221. 
If cell (i, j) is 1, the square submatrice count is the minimal count of cell (i-1, j), cell (i, j-1), cell (i-1, j-1).
"""
# bottom up solution
class Solution:
    def countSquares(self, A: List[List[int]]) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i and j and A[i][j]:
                    A[i][j] = min(A[i][j-1], A[i-1][j], A[i-1][j-1])+1
                ans += A[i][j]
        return ans
                    
# top down solution                    
class Solution:
    def countSquares(self, A: List[List[int]]) -> int: 
        @cache
        def dp(i, j):
            if not (0<=i<len(A) and 0<=j<len(A[0])): return 0
            if A[i][j]==1: return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1))+1
            else: return 0
            
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans += dp(i, j)
        return ans
