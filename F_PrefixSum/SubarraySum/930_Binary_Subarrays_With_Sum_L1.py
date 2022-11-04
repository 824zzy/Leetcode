""" https://leetcode.com/problems/binary-subarrays-with-sum/
subarray sum template
"""
from header import *
class Solution:
    def numSubarraysWithSum(self, A: List[int], k: int) -> int:
        seen = Counter([0])
        prefix = 0
        ans = 0
        
        for x in A:
            prefix += x
            ans += seen[prefix-k]
            seen[prefix] += 1
        return ans