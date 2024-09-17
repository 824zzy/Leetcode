""" https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
Observation: bitwise AND between the maximum and any other number will make the result smaller.

So find longest consecutive subarray of all maximum by groupby.
"""

from header import *


class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        ans = 1
        mx = max(A)
        l = 0
        for i in range(len(A)):
            if A[i] == mx:
                l += 1
            else:
                l = 0
            ans = max(ans, l)
        return ans


# Using groupby
class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        mx = max(A)
        A = [[k, len(list(v))] for k, v in groupby(A)]
        ans = 0
        for k, v in A:
            if k == mx:
                ans = max(v, ans)
        return ans
