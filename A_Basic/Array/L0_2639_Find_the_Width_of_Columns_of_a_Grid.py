""" https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/
simulation
"""


class Solution:
    def findColumnWidth(self, A: List[List[int]]) -> List[int]:
        return [max((len(str(x))) for x in row) for row in zip(*A)]
