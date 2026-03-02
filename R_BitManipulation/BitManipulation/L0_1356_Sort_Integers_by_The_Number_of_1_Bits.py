""" https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""


class Solution:
    def sortByBits(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: (x.bit_count(), x))
