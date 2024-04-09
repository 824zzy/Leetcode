""" https://leetcode.com/problems/intersection-of-two-arrays
find unordered intersection by set operation
"""


class Solution:
    def intersection(self, A: List[int], B: List[int]) -> List[int]:
        return set(A) & set(B)
