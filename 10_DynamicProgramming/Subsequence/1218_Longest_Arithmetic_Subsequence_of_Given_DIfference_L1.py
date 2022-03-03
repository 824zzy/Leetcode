""" https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
Sweep through arr and check the longest arithemetic subsequence ending at current value.
"""
class Solution:
    def longestSubsequence(self, A: List[int], diff: int) -> int:
        ans = 0
        seen = {}
        for x in A:
            seen[x] = 1+seen.get(x-diff, 0)
            ans = max(ans, seen[x])
        return ans