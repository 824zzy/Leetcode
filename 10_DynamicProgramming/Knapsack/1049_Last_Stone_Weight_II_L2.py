""" https://leetcode.com/problems/last-stone-weight-ii/
Intuition: the final answer as a sum of weights with + or - sign symbols infront of each weight.

for each weight, apply dp to find minimum summation when either add + sign or - sign.
"""
class Solution:
    def lastStoneWeightII(self, A: List[int]) -> int:
        @cache
        def dp(i, sm):
            if i==len(A): return abs(sm)
            return min(dp(i+1, sm+A[i]), dp(i+1, sm-A[i]))
        
        return dp(0, 0)