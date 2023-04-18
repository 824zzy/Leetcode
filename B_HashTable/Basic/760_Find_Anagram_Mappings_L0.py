"""https://leetcode.com/problems/find-anagram-mappings/
Use a dictionary to store the index of each element in nums2.
"""
from header import *

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = defaultdict(list)
        for i, x in enumerate(nums2):
            mp[x].append(i)
            
        return [mp[x].pop() for x in nums1]