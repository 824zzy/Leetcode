""" https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
1. For each cell, we check if the 3 bottom cell are all 1, if yes, then it is a fertile cell. 
2. Then we use minimum of the 3 bottom cells to calculate the number of fertile cells.
Time complexity: O(m*n)
"""
class Solution:
    def countPyramids(self, A: List[List[int]]) -> int:
        @cache
        def dp(i, j):
            if not (0<=i<len(A) and 0<=j<len(A[0])): return 0
            if A[i][j]==0: return 0
            if i+1<len(A) and 0<=j-1<j+1<len(A[0]) and A[i+1][j-1] and A[i+1][j] and A[i+1][j+1]:
                return 1+min(dp(i+1, j-1), dp(i+1, j), dp(i+1, j+1))
            else: return 0

        
        ans = sum([dp(i, j) for i in range(len(A)) for j in range(len(A[0]))])
        A = A[::-1]
        dp.cache_clear()
        return ans+sum([dp(i, j) for i in range(len(A)) for j in range(len(A[0]))])