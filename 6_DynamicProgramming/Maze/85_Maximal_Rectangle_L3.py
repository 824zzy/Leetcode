""" https://leetcode.com/problems/maximal-rectangle/
"""
class Solution:
    def maximalRectangle(self, A: List[List[str]]) -> int:
        if not A: return 0
        m, n = len(A), len(A[0])
        
        @lru_cache(None)
        def height(i, j):
            if i < 0 or A[i][j] == "0": return 0
            return 1 + height(i-1, j)
        
        @lru_cache(None)
        def left(i, j): 
            if j == -1 or A[i][j] == "0": return j+1
            return left(i, j-1)
        
        @lru_cache(None)
        def lo(i, j): 
            if i < 0 or A[i][j] == "0": return 0
            return max(lo(i-1, j), left(i, j))
        
        @lru_cache(None)
        def right(i, j):
            if j == n or A[i][j] == "0": return j
            return right(i, j+1)
        
        @lru_cache(None)
        def hi(i, j):
            if i < 0 or A[i][j] == "0": return n
            return min(hi(i-1, j), right(i, j))
        
        return max(height(i, j)*(hi(i, j) - lo(i, j)) for i in range(m) for j in range(n))