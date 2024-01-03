""" https://leetcode.com/problems/binary-subarrays-with-sum/
presum[j]-presum[i] = t
===> presum[j]-t = presum[i]
"""
from header import *

class Solution:
    def numSubarraysWithSum(self, A: List[int], t: int) -> int:
        cnt = Counter([0])
        ans = pre = 0
        for x in A:
            pre += x
            ans += cnt[pre-t]
            cnt[pre] += 1
        return ans