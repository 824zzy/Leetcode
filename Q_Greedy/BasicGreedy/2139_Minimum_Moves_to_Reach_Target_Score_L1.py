""" https://leetcode.com/problems/minimum-moves-to-reach-target-score/
think reversely, reduce t to 1
"""
class Solution:
    def minMoves(self, t: int, k: int) -> int:
        ans = 0
        while t>1 and k>0:
            ans += 1
            if t&1: t -= 1
            else: t, k = t//2, k-1
        return ans+t-1