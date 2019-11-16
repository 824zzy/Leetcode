# TWo dimention solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]
        dp[-1] = triangle[-1]
        for i, raw in enumerate(triangle[:-1][::-1]):
            for j in range(len(raw)):
                up, down = len(triangle)-2-i, len(triangle)-1-i
                dp[up][j] = min(dp[down][j], dp[down][j+1])+ triangle[up][j]
        return dp[0][0]

# One dimention solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)
        for raw in triangle[::-1]:
            for i in range(len(raw)):
                dp[i] = raw[i] + min(dp[i], dp[i+1])
        return dp[0]