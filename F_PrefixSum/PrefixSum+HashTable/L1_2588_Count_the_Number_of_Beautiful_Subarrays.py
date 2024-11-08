""" https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/
convert the problem into: find all the subarrays that elements  XOR=0
"""

from header import *


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # prefix XOR
        A = [0]
        for x in nums:
            A.append(A[-1] ^ x)

        cnt = Counter()
        ans = 0
        for x in A:
            ans += cnt[x]
            cnt[x] += 1
        return ans


class Solution:
    def beautifulSubarrays(self, A: List[int]) -> int:
        cnt = Counter([0])
        mask = 0
        ans = 0
        for x in A:
            mask ^= x
            ans += cnt[mask]
            cnt[mask] += 1
        return ans
