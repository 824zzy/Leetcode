""" https://leetcode.com/problems/stone-game-iii/
minimax
"""
class Solution:
    def stoneGameIII(self, A: List[int]) -> str:
        @cache
        def dp(i):
            if i>=len(A): return 0
            ans = -inf
            for j in (1, 2, 3):
                ans = max(ans, sum(A[i:i+j])-dp(i+j))
            return ans
        
        ans = dp(0)
        if ans>0: return "Alice"
        elif ans<0: return "Bob"
        else: return "Tie"