""" TODO: 2hard, cry
"""
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon[0])
        need = [2**31] * (n-1) + [1]
        
        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                need[j] = max(min(need[j:j+2]) - row[j], 1)
                
        return need[0]


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [[2**31 for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        
        return dp[0][0]