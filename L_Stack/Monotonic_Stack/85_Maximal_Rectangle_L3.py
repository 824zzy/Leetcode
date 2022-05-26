""" https://leetcode.com/problems/maximal-rectangle/
DP + Monotonic stack(84)
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        maxArea = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == "1": dp[c] += 1
                else: dp[c] = 0
            maxArea = max(maxArea, self.maxRectangleInHistogram(dp))
        return maxArea
    
    def maxRectangleInHistogram(self, A):  # O(N)
        s, ans = [], 0
        for i, h in enumerate(A+[0]):
            while s and h<=A[s[-1]]:
                H = A[s.pop()]
                W = i if not s else i-s[-1]-1
                ans = max(ans, H*W)
            s.append(i)
        return ans