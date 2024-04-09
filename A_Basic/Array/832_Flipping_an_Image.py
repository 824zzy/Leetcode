""" L0: https://leetcode.com/problems/flipping-an-image/
reverse and flip array
"""


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[0 if i else 1 for i in a[::-1]] for a in A]
