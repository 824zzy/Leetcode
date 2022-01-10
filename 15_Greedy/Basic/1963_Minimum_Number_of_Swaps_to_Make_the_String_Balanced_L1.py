""" https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
# find maximum disbalance
"""
class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        prefix = 0
        for c in s:
            if c=='[': prefix -= 1
            else: prefix += 1
            # find maximum disbalance
            ans = max(ans, prefix)
        return ceil((ans)/2)