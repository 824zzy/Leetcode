class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)
        for raw in triangle[::-1]:
            for i in range(len(raw)):
                dp[i] = raw[i] + min(dp[i], dp[i+1])

        return dp[0]