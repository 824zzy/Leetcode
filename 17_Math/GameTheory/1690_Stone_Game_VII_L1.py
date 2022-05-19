""" https://leetcode.com/problems/stone-game-vii/
time sequential dp + minimax
"""
class Solution:
    def stoneGameVII(self, A: List[int]) -> int:
        A = list(accumulate(A, initial=0))
        
        @cache
        def dp(l, r):
            if l==r: return 0
            ll = (A[r]-A[l+1])-dp(l+1, r)
            rr = (A[r-1]-A[l])-dp(l, r-1)
            return max(ll, rr)
        
        ans = dp(0, len(A)-1)
        dp.cache_clear()
        return ans