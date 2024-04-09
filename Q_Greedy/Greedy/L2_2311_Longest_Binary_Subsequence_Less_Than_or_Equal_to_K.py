""" https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
Greedy heuristic: from left to right, remove as many 1 as possible until s is less or equal than k
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = int(s, 2)
        cnt = 0

        for i in range(len(s)):
            if n <= k:
                return len(s) - cnt
            if s[i] == '1':
                n -= 1 << (len(s) - i - 1)
                cnt += 1
