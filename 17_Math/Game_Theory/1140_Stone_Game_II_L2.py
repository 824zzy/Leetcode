""" https://leetcode.com/problems/stone-game-ii/
from ye15: https://leetcode.com/problems/stone-game-ii/discuss/530127/Python3-top-down-dp
Define fn(i, m) as the net winning stones when a player is at i with m. Let X and Y be Alex and Lee's stones respectively. Then,
X - Y = fn(0, 1) and X + Y = sum(piles).
As a result, X = (fn(0, 1) + sum(piles))//2.
"""
class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        @cache
        def dp(i, M):
            if i+2*M>=len(A): return sum(A[i:])
            ans = -inf
            for j in range(i+1, i+2*M+1):
                ans = max(ans, sum(A[i:j])-dp(j, max(j-i, M)))
            return ans
            
        return (dp(0, 1)+sum(A))//2