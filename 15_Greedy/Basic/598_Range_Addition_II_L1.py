""" https://leetcode.com/problems/range-addition-ii/
find minimum value of top left corner
"""
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m*n
        min_m, min_n = min([o[0] for o in ops]), min([o[1] for o in ops])
        return min_m*min_n