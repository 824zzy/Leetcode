""" https://leetcode.com/problems/longest-happy-prefix/
greedily find prefix and suffix from large window to small window.
"""


class Solution:
    def longestPrefix(self, A: str) -> str:
        for i in reversed(range(1, len(A))):
            if A[:i] == A[-i:]:
                return A[:i]
        return ""
