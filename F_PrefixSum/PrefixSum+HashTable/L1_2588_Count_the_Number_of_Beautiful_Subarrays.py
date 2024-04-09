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


# solution that not using XOR
class Solution:
    def beautifulSubarrays(self, A: List[int]) -> int:
        seen = [0] * 20
        cnt = Counter()
        cnt[tuple(seen)] = 1
        ans = 0
        for x in A:
            i = 0
            while x:
                if x & 1:
                    seen[i] += 1
                    seen[i] %= 2
                x >>= 1
                i += 1
            ans += cnt[tuple(seen)]
            cnt[tuple(seen)] += 1
        return ans
