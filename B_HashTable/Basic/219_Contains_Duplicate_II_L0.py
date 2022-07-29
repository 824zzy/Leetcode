""" https://leetcode.com/problems/contains-duplicate-ii/
"""
class Solution:
    def containsNearbyDuplicate(self, A: List[int], k: int) -> bool:
        seen = {}
        for i, x in enumerate(A):
            if x in seen and i-seen[x]<=k: return True
            seen[x] = i
        return False