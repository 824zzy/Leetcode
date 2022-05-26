""" https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
Increasing n - 1 smaller elements by 1 = decreasing only the max element by 1
"""
class Solution:
    def minMoves(self, A: List[int]) -> int:
        ans = 0
        mi = min(A)
        for x in A: ans += x-mi
        return ans