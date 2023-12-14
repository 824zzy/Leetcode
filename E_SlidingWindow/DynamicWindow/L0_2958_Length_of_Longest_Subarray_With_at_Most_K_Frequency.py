""" https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
sliding window template
"""
from header import *

class Solution:
    def maxSubarrayLength(self, A: List[int], k: int) -> int:
        cnt = Counter()
        ans = 0
        i = 0
        for j in range(len(A)):
            cnt[A[j]] += 1
            while cnt[A[j]]>k:
                cnt[A[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
        return ans
        