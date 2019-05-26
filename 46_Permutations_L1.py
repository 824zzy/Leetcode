""" usage of itertools
1. list(permutations(nums))
"""

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rv = list(permutations(nums))
        for i in range(len(rv)):
            rv[i] = list(rv[i])
        return rv
        