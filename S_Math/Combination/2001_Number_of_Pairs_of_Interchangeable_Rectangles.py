""" L0: https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
Gaussian bless us
"""
class Solution:
    def interchangeableRectangles(self, A: List[List[int]]) -> int:
        M = Counter()
        for i, j in A: M[i/j] += 1
        return int(sum([v*(v-1)/2 for _, v in M.items()]))