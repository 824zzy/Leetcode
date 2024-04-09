""" https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/
check num is between min and max or now
"""


class Solution:
    def countElements(self, A: List[int]) -> int:
        mi, ma = min(A), max(A)
        return sum(mi < x < ma for x in A)
