""" https://leetcode.com/problems/contains-duplicate-ii/
linear scan, check if the element is in the `seen` and update `seen`
"""
from header import *

class Solution:
    def containsNearbyDuplicate(self, A: List[int], k: int) -> bool:
        seen = {}
        for i, x in enumerate(A):
            if x in seen and i-seen[x]<=k: return True
            seen[x] = i
        return False