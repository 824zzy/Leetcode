""" https://leetcode.com/problems/shortest-palindrome/
greedily find longest palindrome start from idx 0
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s
