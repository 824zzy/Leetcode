""" https://leetcode.com/problems/contiguous-array/
consider 0 as -1:
    presum[j]-presum[i] = 0 ===> presum[j] = presum[i]
"""
from header import *


class Solution:
    def findMaxLength(self, A: List[int]) -> int:
        cnt = Counter()
        cnt[0] = -1
        ans = 0
        pre = 0
        for i, x in enumerate(A):
            if x == 0:
                pre -= 1
            else:
                pre += 1
            if pre in cnt:
                ans = max(ans, i - cnt[pre])
            cnt.setdefault(pre, i)
        return ans
