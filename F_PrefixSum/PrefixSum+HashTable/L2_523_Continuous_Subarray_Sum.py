""" https://leetcode.com/problems/continuous-subarray-sum/submissions/
the same as 525 except use prefix modulo
1. compute prefix modulo
2. use seen to record the first occurrence of prefix modulo
3. if a prefix modulo has appeared before, it indicates that a piece of subarray sums is k.
"""
from header import *

class Solution:
    def checkSubarraySum(self, A: List[int], k: int) -> bool:
        seen = {0: -1}
        prefix = 0
        
        for i, x in enumerate(A):
            prefix = (prefix+x) % k
            seen.setdefault(prefix, i)
            if prefix in seen and i-seen[prefix]>1: 
                return True
        return False