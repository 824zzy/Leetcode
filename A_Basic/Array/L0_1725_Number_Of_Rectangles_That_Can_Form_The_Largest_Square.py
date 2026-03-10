""" https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
"""

class Solution:
    def countGoodRectangles(self, A: List[List[int]]) -> int:
        mins = [min(a) for a in A]
        t = max(mins)
        return mins.count(t)
