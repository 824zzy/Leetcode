""" https://leetcode.com/problems/k-inverse-pairs-array/
Define the dp(n, k) state as the number of permutations from 1...n that has exactly k inverse.
Given:
dp(n, k) = dp(n-1, k) + dp(n-1, k-1) + dp(n-1, k-2) + ... + dp(n-1, k-(n-2)) + dp(n-1, k-(n-1)), where k-(n-1)>=0
dp(n, k-1) = dp(n-1, k-1) + dp(n-1, k-2) + dp(n-1, k-3) + ... + dp(n-1, k-(n-1)) + dp(n-1, k-n), where k-n>=0

We can obtain
dp(n, k) - dp(n, k-1) = dp(n-1, k) - dp(n-1, k-n)
dp(n, k) = dp(n, k-1) + dp(n-1, k) - dp(n-1, k-n)
"""
from header import *

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(n, k):
            if k==0: return 1
            if n<=0 or k<0: return 0
            return (dp(n-1, k)+dp(n, k-1)-dp(n-1, k-n)) % MOD
        
        return dp(n, k) % MOD