"""
"""
# A tricky one line permutation by permutation
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))

# TODO: add the back-tracking solution