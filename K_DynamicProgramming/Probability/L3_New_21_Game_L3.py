""" https://leetcode.com/problems/new-21-game/
learn from ye and https://www.youtube.com/watch?v=bd0t6cj7_4E

Define dp(n) as the probability of points between K and N, i.e. [K, N] given existing point n. Then,

if n < K, dp(n) = 1/W*(dp(n+1) + dp(n+2) + ... + dp(n+W));
if K <= n <= N, dp(n) = 1;
if N < n, dp(n) = 0.
Trick: if n+1 < K, then from
dp(n) = 1/W*(dp(n+1) + dp(n+2) + ... + dp(n+W))
dp(n+1) = 1/W*(dp(n+2) + dp(n+3) + ... + dp(n+W+1))
one can derive dp(n) = (1+W)/W*dp(n) - 1/W*dp(n+W+1). When n+1 == K, this trick cannot be applied as the relationship of dp(n+1) = 1/W*(dp(n+2) + ...) doesn't hold in general.
"""
from header import *

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        @cache
        def dp(i):
            if i>N: return 0
            elif K<=i<=N: return 1
            elif i+1<K: return dp(i+1)-(dp(i+W+1)-dp(i+1))/W
            else:
                return 1/W*sum(dp(j) for j in range(i+1, i+W+1))
        
        return dp(0)