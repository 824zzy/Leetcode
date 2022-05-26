""" https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
find the longest path in the graph by maze dp
"""
class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        D = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        @cache
        def dp(x, y):
            ans = 1
            for dx, dy in D:
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]) and A[x+dx][y+dy]>A[x][y]:
                    ans = max(ans, 1+dp(x+dx, y+dy))
            return ans
        
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans = max(ans, dp(i, j))
        return ans