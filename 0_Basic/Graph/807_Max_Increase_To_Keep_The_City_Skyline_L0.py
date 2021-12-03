""" https://leetcode.com/problems/max-increase-to-keep-city-skyline/
increased height is regard to minimum skyline of current row and column.
min(lr, td)-A[i][j]
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, A: List[List[int]]) -> int:
        LR = [max(r) for r in A]
        TD = [max(c) for c in zip(*A)]
        
        ans = 0
        for i, lr in enumerate(LR):
            for j, td in enumerate(TD):
                ans += min(lr, td)-A[i][j]
        return ans