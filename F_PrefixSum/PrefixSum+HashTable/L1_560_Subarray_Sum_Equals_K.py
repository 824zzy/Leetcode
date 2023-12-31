""" https://leetcode.com/problems/subarray-sum-equals-k/
subarray sum template
"""
from header import *

class Solution:
    def subarraySum(self, A: List[int], k: int) -> int:
        cnt = Counter([0])
        prefix = 0
        ans = 0
        
        for x in A:
            prefix += x
            ans += cnt[prefix-k]
            cnt[prefix] += 1
        return ans